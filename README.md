# Asia on Plate Customer Service Bot

A sophisticated multi-agent customer service system built for Asia on Plate, an Asian grocery delivery service in Berlin. The system uses AWS Bedrock, Pinecone vector database, and Tavily web search to provide intelligent customer support through a modern Gradio web interface.

## System Architecture

The bot implements a three-agent architecture:

1. **Query Analyzer Agent**: Analyzes customer queries to determine intent and extract key information
2. **Information Retriever Agent**: Searches multiple data sources for relevant information
3. **Response Generator Agent**: Creates contextual, helpful responses based on retrieved information

## Features

### Core Capabilities
- Multi-language support (English and German)
- Order tracking and status updates
- Product information and recommendations
- Delivery and return policy assistance
- Account management support
- Conversation state management for follow-up queries

### Web Interface
- Modern Gradio-based chat interface
- Real-time message exchange
- Message history and conversation state
- Example queries for easy testing
- Responsive design for all devices

### Data Sources
- Internal order database (JSON)
- Knowledge base (comprehensive support guide)
- Vector database (Pinecone) for semantic search
- Web search (Tavily API) for external information

### Advanced Features
- Conversation memory for multi-turn interactions
- Intelligent query classification
- Missing information detection
- Escalation handling
- Real-time order status tracking

## Project Structure

```
langchain_basics/
├── agents/
│   ├── query_analyzer.py           # Query analysis and classification
│   ├── information_retriever.py    # Multi-source information retrieval
│   └── response_generator.py       # Contextual response generation
├── data/
│   ├── orders.json                 # Sample order database
│   └── support_guide.txt           # Comprehensive knowledge base
├── utils/
│   └── bedrock_client.py           # AWS Bedrock client utilities
├── static/                         # Static files (if needed)
├── app.py                          # Gradio web application
├── main.py                         # Core bot logic
├── config.py                       # Configuration management
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── start.sh                        # Deployment startup script
└── README.md                       # This file
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- AWS account with Bedrock access
- Pinecone account and API key
- Tavily API key for web search

### Local Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/parthsharma1011/langchain_.git
cd langchain_
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Environment Configuration:**
```bash
# Copy the environment template
cp .env.example .env

# Edit .env with your actual API keys
nano .env
```

4. **Configure your .env file:**
```env
# AWS Bedrock Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0

# External Services
TAVILY_API_KEY=your_tavily_api_key
PINECONE_API_KEY=your_pinecone_api_key

# Agent Settings
MAX_TOKENS=2048
TEMPERATURE=0.7
```

5. **Ensure AWS Bedrock access:**
   - Enable Bedrock in your AWS region
   - Request access to Claude models
   - Verify IAM permissions for Bedrock

## Usage

### Running Locally

**Start the Gradio web interface:**
```bash
python app.py
```

**Access the application:**
- Open browser to `http://localhost:7860`
- You'll see a professional chat interface

**Command line interface (optional):**
```bash
python main.py
```

### Example Interactions

**Order Tracking:**
```
Customer: I want to track my order 12345
Bot: Your order 12345 has been delivered. Items: Shin Ramyun x3, Kimchi 500g, Soy Sauce. Total: Euro15.47. Tracking: DHL123456789
```

**Product Information:**
```
Customer: Do you have organic products?
Bot: Yes! We stock organic versions of rice, noodles, sauces, and snacks. Look for the "BIO" label on our website.
```

**Multi-turn Conversation:**
```
Customer: I need to track my order
Bot: I'd be happy to help you track your order. Could you please provide your order ID or your email address and full name?
Customer: john@example.com
Bot: I found your order! Order 12345: Status - delivered, Items - Shin Ramyun x3, Kimchi 500g, Soy Sauce...
```

## Deployment

### Render Cloud Deployment

1. **Push to GitHub** (ensure .env is in .gitignore)

2. **On Render.com:**
   - Connect your GitHub repository
   - Choose "Web Service"
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3

3. **Set Environment Variables on Render:**
   ```
   AWS_ACCESS_KEY_ID=your_actual_key
   AWS_SECRET_ACCESS_KEY=your_actual_secret
   AWS_REGION=us-east-1
   BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
   TAVILY_API_KEY=your_actual_key
   PINECONE_API_KEY=your_actual_key
   MAX_TOKENS=2048
   TEMPERATURE=0.7
   ```

4. **Deploy** - Render will provide a public URL

### Other Deployment Options

**Heroku:**
```bash
# Add Procfile
echo "web: python app.py" > Procfile
```

**Docker:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]
```

## Configuration Options

### Model Parameters
```env
MAX_TOKENS=2048           # Maximum response length
TEMPERATURE=0.7           # Response creativity (0.0-1.0)
BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0  # Model selection
```

### Agent Behavior
- Query classification confidence thresholds
- Information retrieval settings
- Conversation management parameters

## Data Management

### Order Database Structure
```json
{
  "orders": [
    {
      "order_id": "12345",
      "customer_email": "john@example.com",
      "customer_name": "John Smith",
      "status": "delivered",
      "items": ["Shin Ramyun x3", "Kimchi 500g", "Soy Sauce"],
      "total": 15.47,
      "tracking": "DHL123456789"
    }
  ]
}
```

### Knowledge Base
Comprehensive support guide covering:
- Product catalog and pricing
- Delivery information and policies
- Return and refund procedures
- Payment options
- Account management
- Contact information

## Code Audit Summary

### Architecture Strengths
- **Clean Multi-Agent Design**: Well-separated concerns with distinct agent responsibilities
- **Conversation Management**: Effective state handling for multi-turn conversations
- **Multiple Data Sources**: Comprehensive information retrieval from various sources
- **Modern Web Interface**: Professional Gradio-based chat interface
- **Environment Security**: Proper API key management with environment variables

### Security Features
- API keys stored in environment variables
- .env file excluded from version control
- Secure deployment configuration
- Input validation and error handling

### Performance Considerations
- Efficient conversation state management
- Optimized API calls with proper error handling
- Responsive web interface
- Scalable architecture for deployment

## API Keys and Security

### Required API Keys
1. **AWS Bedrock**: Access Key ID and Secret Access Key
2. **Tavily**: API key for web search functionality
3. **Pinecone**: API key for vector database operations

### Security Best Practices
- Never commit API keys to version control
- Use environment variables for all sensitive data
- Implement proper error handling for API failures
- Use HTTPS for all external communications
- Regular key rotation recommended

## Troubleshooting

### Common Issues

**Environment Variables Not Loading:**
```bash
# Ensure python-dotenv is installed
pip install python-dotenv

# Check .env file exists and has correct format
cat .env
```

**Gradio Interface Not Starting:**
```bash
# Check port availability
lsof -i :7860

# Try different port
PORT=8080 python app.py
```

**AWS Bedrock Access Issues:**
- Verify AWS credentials and permissions
- Check Bedrock model access in AWS console
- Ensure correct region configuration

**API Rate Limits:**
- Implement exponential backoff
- Monitor API usage
- Consider caching frequent queries

### Debug Mode
```python
# Enable detailed logging
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

## Performance Optimization

### Recommended Improvements
1. **Implement Caching**: Redis or in-memory caching for frequent queries
2. **Async Operations**: Make API calls asynchronous for better performance
3. **Enhanced Embeddings**: Use sentence-transformers instead of simple word count
4. **Connection Pooling**: Optimize database and API connections
5. **Load Balancing**: For high-traffic deployments

## Testing

### Local Testing
```bash
# Test the web interface
python app.py

# Test command line interface
python main.py

# Test individual components
python -c "from agents.query_analyzer import QueryAnalyzerAgent; print('Import successful')"
```

### Example Test Queries
- "I want to track my order 12345"
- "Do you have Korean kimchi?"
- "What are your delivery hours?"
- "How can I return an item?"
- "john@example.com" (for follow-up queries)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper testing
4. Update documentation as needed
5. Submit a pull request with detailed description

## License

This project is licensed under the MIT License.

## Support

For technical support or questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Ensure all dependencies are properly installed
- Verify API keys and configurations are correct

## Acknowledgments

- AWS Bedrock for LLM capabilities
- Pinecone for vector database services
- Tavily for web search functionality
- Gradio for the modern web interface
- The LangChain community for inspiration and best practices

## Version History

- **v1.0.0**: Initial release with multi-agent architecture
- **v1.1.0**: Added Gradio web interface
- **v1.2.0**: Implemented environment variable security
- **Current**: Enhanced documentation and deployment guides