# 🚀 Bedrock Learning Hub

Comprehensive learning repository for AWS Bedrock services with multiple AI models and practical examples.

## 🎯 What You'll Learn
- AWS Bedrock API integration
- Multiple AI model providers (Anthropic, Amazon, Meta, Cohere)
- Progressive tutorials from basic to advanced
- Real-world examples and best practices

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google API Key (for Gemini)
- AWS Credentials (for Bedrock)

### Installation
```bash
git clone https://github.com/parthsharma1011/langchain_.git
cd langchain_
pip install -r requirements.txt
```

## 📁 Project Structure

```
langchain_/
├── langchain_example.py    # Main examples file
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 🔧 Setup

### 1. Google Gemini API
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. Replace `YOUR_GOOGLE_API_KEY` in the code

### 2. AWS Bedrock (Optional)
1. Create AWS account
2. Get Access Key ID and Secret Access Key
3. Ensure Bedrock access in your region

## 💡 Examples Included

### 1. Basic LangChain with Google Gemini
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="YOUR_API_KEY",
    temperature=0.7,
    max_output_tokens=1000
)

response = llm.invoke("Explain machine learning")
print(response)
```

### 2. ReAct Agent with Tools
The code includes a ReAct (Reasoning + Acting) agent that can:
- Perform mathematical calculations
- Look up pill weights
- Chain reasoning steps

### 3. RAG (Retrieval Augmented Generation)
- Vector database with FAISS
- Document embedding and similarity search
- Context-aware responses

## 🏃‍♂️ Running the Examples

### Run Basic Examples
```bash
python langchain_example.py
```

### Uncomment Sections
The main file has different sections commented out. Uncomment the section you want to run:

1. **Basic Gemini Integration** (Lines 1-17)
2. **ReAct Agent** (Lines 19-123)
3. **RAG Implementation** (Lines 125+)

## 🔑 Environment Variables (Recommended)

Create a `.env` file:
```bash
GOOGLE_API_KEY=your_google_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

Then load in your code:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

## 📚 Key Concepts Demonstrated

### LangChain Components
- **LLMs**: Language model integration
- **Agents**: Autonomous reasoning systems
- **Tools**: External function calling
- **Memory**: Conversation history management
- **Embeddings**: Text vectorization
- **Vector Stores**: Similarity search

### ReAct Pattern
```
Thought: I need to calculate something
Action: calculate: 2 + 2
Observation: 4
Thought: Now I have the answer
Answer: The result is 4
```

### RAG Pipeline
1. **Document Loading**: Text → Document objects
2. **Embedding**: Documents → Vectors
3. **Storage**: Vectors → Vector Database
4. **Retrieval**: Query → Similar documents
5. **Generation**: Context + Query → Response

## 🛠️ Customization

### Adding New Tools
```python
def your_custom_tool(input_text):
    # Your logic here
    return result

known_actions = {
    "calculate": calculate,
    "your_tool": your_custom_tool
}
```

### Changing Models
```python
# For different Gemini models
model="gemini-1.5-pro"  # More powerful
model="gemini-1.5-flash"  # Faster

# For different temperatures
temperature=0.1  # More focused
temperature=0.9  # More creative
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your Google API key is valid
   - Check API quotas and billing

2. **Import Errors**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.8+)

3. **Memory Issues**
   - Reduce `max_output_tokens`
   - Use smaller embedding models

### Debug Mode
Add this for detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Tips

1. **Optimize Token Usage**
   - Set appropriate `max_tokens`
   - Use shorter prompts when possible

2. **Caching**
   - Cache embeddings for repeated use
   - Store vector databases locally

3. **Batch Processing**
   - Process multiple documents together
   - Use async operations for parallel calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Useful Links

- [LangChain Documentation](https://python.langchain.com/)
- [Google AI Studio](https://makersuite.google.com/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [FAISS Documentation](https://faiss.ai/)

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review the error messages carefully
3. Ensure all API keys are correctly configured
4. Verify all dependencies are installed

---

**Happy coding with LangChain! 🎉**