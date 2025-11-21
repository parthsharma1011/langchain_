"""
Basic Chat Examples with Different Models
"""
import sys
sys.path.append('..')

from models.anthropic.claude_haiku import ClaudeHaiku

def test_basic_chat():
    """Test basic chat functionality"""
    print("🚀 Testing Basic Chat with Claude Haiku")
    print("="*50)
    
    haiku = ClaudeHaiku()
    
    questions = [
        "What is AWS Bedrock?",
        "Explain machine learning in simple terms",
        "Write a Python function to add two numbers"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. Question: {question}")
        print("-" * 40)
        
        response = haiku.chat(question, max_tokens=200)
        if response:
            print(f"🤖 Answer: {response}")
        else:
            print("❌ No response received")

if __name__ == "__main__":
    test_basic_chat()