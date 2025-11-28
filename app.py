import gradio as gr
from main import AsiaonPlateBot
import os

# Initialize the bot
bot = AsiaonPlateBot()

def chat_with_bot(message, history):
    """
    Process user message and return bot response
    """
    try:
        # Get bot response
        response = bot.process_query(message)
        
        # Add to history
        history.append([message, response])
        
        return history, ""
    except Exception as e:
        error_msg = f"Sorry, I encountered an error: {str(e)}"
        history.append([message, error_msg])
        return history, ""

def reset_conversation():
    """Reset the conversation state"""
    global bot
    bot = AsiaonPlateBot()  # Reinitialize bot to reset state
    return []

# Create Gradio interface
with gr.Blocks(title="Asia on Plate Customer Service", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🍜 Asia on Plate Customer Service Bot
        
        Welcome to Asia on Plate! I can help you with:
        - Order tracking and status updates
        - Product information and recommendations  
        - Delivery and return policies
        - Account management
        - General questions about our Asian grocery service
        
        **Languages supported:** English and German
        """
    )
    
    # Chat interface
    chatbot = gr.Chatbot(
        value=[],
        height=400,
        show_label=False,
        container=True,
        bubble_full_width=False
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here... (e.g., 'Track my order 12345')",
            show_label=False,
            scale=4,
            container=False
        )
        submit_btn = gr.Button("Send", variant="primary", scale=1)
    
    with gr.Row():
        clear_btn = gr.Button("Clear Chat", variant="secondary")
        reset_btn = gr.Button("Reset Conversation", variant="secondary")
    
    # Event handlers
    def submit_message(message, history):
        if message.strip():
            return chat_with_bot(message, history)
        return history, message
    
    # Submit on button click
    submit_btn.click(
        submit_message,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )
    
    # Submit on Enter key
    msg.submit(
        submit_message,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )
    
    # Clear chat history
    clear_btn.click(
        lambda: [],
        outputs=chatbot
    )
    
    # Reset conversation state
    reset_btn.click(
        reset_conversation,
        outputs=chatbot
    )
    
    # Example queries
    gr.Examples(
        examples=[
            "I want to track my order 12345",
            "Do you have Korean kimchi?",
            "What are your delivery hours?",
            "How can I return an item?",
            "john@example.com"  # For follow-up after order tracking
        ],
        inputs=msg,
        label="Try these example queries:"
    )

# Launch the app
if __name__ == "__main__":
    # Get port from environment (for deployment) or use default
    port = int(os.environ.get("PORT", 7860))
    
    demo.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=port,       # Use environment port or default
        share=False,            # Set to True for temporary public link
        debug=False             # Disable debug in production
    )