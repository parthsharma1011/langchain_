# Asia on Plate Customer Service Bot

A sophisticated multi-agent customer service system built for Asia on Plate, an Asian grocery delivery service in Berlin. The system uses AWS Bedrock, Pinecone vector database, and Tavily web search to provide intelligent customer support.

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
proj_2/
├── agents/
│   ├── query_analyzer.py           # Query analysis and classification
│   ├── information_retriever.py    # Multi-source information retrieval
│   └── response_generator.py       # Contextual response generation
├── data/
│   ├── orders.json                 # Sample order database
│   └── support_guide.txt           # Comprehensive knowledge base
├── utils/
│   └── bedrock_client.py           # AWS Bedrock client utilities
├── config.py                       # Configuration and API keys
├── main.py                         # Main application entry point
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- AWS account with Bedrock access
- Pinecone account and API key
- Tavily API key for web search

### Installation Steps

1. Clone the repository and navigate to proj_2:
```bash
cd proj_2
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure API keys in config.py:
```python
class Config:
    # AWS Bedrock Configuration
    AWS_ACCESS_KEY_ID = "your_aws_access_key"
    AWS_SECRET_ACCESS_KEY = "your_aws_secret_key"
    AWS_REGION = "us-east-1"
    BEDROCK_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
    
    # External Services
    TAVILY_API_KEY = "your_tavily_api_key"
    PINECONE_API_KEY = "your_pinecone_api_key"
    
    # Agent Settings
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7
```

4. Ensure AWS Bedrock access:
   - Enable Bedrock in your AWS region
   - Request access to Claude models
   - Verify IAM permissions for Bedrock

## Usage

### Running the Interactive Bot
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

## Configuration Options

### Model Parameters
```python
MAX_TOKENS = 2048           # Maximum response length
TEMPERATURE = 0.7           # Response creativity (0.0-1.0)
```

### Agent Behavior
```python
# Query classification confidence thresholds
CLASSIFICATION_THRESHOLD = 0.8

# Information retrieval settings
MAX_SEARCH_RESULTS = 3
SIMILARITY_THRESHOLD = 0.7

# Conversation management
MAX_CONVERSATION_TURNS = 10
```

## Data Management

### Order Database Structure
The system uses a JSON file to simulate an order database:
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

## Agent Details

### Query Analyzer Agent
**Purpose**: Analyzes customer queries to determine intent and extract key information

**Capabilities**:
- Query type classification (order_tracking, product_info, delivery_info, etc.)
- Key information extraction (order IDs, customer details)
- Missing information identification
- Urgency assessment
- Multi-language support (English/German)

### Information Retriever Agent
**Purpose**: Retrieves relevant information from multiple data sources

**Data Sources**:
- Internal order database lookup
- Knowledge base semantic search
- Pinecone vector database
- Tavily web search API
- Fallback text similarity search

**Search Methods**:
- Exact order ID matching
- Customer name/email fuzzy matching
- Semantic similarity search
- Keyword-based text search
- External web search when needed

### Response Generator Agent
**Purpose**: Creates contextual, helpful responses based on retrieved information

**Features**:
- Context-aware response generation
- Multi-language response capability
- Missing information handling
- Source attribution
- Professional tone maintenance
- Escalation recommendations

## Performance Considerations

### Optimization Strategies
- Implement response caching for common queries
- Use connection pooling for database operations
- Batch vector operations when possible
- Implement async operations for external API calls

### Monitoring and Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Error Handling Best Practices
- Implement retry logic for API failures
- Use circuit breakers for external services
- Provide graceful degradation when services are unavailable
- Log errors with sufficient context for debugging

## Testing

### Unit Testing
Test individual agent components:
```bash
python -m pytest tests/test_query_analyzer.py
python -m pytest tests/test_information_retriever.py
python -m pytest tests/test_response_generator.py
```

### Integration Testing
Test the complete workflow:
```bash
python -m pytest tests/test_integration.py
```

### Manual Testing
Test specific scenarios:
```python
# Test order tracking
bot = AsiaonPlateBot()
response = bot.process_query("Track order 12345")
print(response)

# Test product inquiry
response = bot.process_query("Do you have Korean kimchi?")
print(response)
```

## Deployment Considerations

### Production Deployment
- Use environment variables for sensitive configuration
- Implement proper logging and monitoring
- Set up health checks and alerting
- Use containerization (Docker) for consistent deployment
- Implement load balancing for high availability

### Security Best Practices
- Never commit API keys to version control
- Use AWS IAM roles instead of access keys when possible
- Implement rate limiting to prevent abuse
- Validate and sanitize all user inputs
- Use HTTPS for all external communications

## Troubleshooting

### Common Issues

**Bot not responding:**
- Check AWS Bedrock credentials and permissions
- Verify internet connectivity for external APIs
- Check log files for error messages

**Poor response quality:**
- Adjust temperature settings in config.py
- Review and update knowledge base content
- Fine-tune prompt engineering in agents

**Slow performance:**
- Implement caching for frequent queries
- Optimize vector database operations
- Consider using faster embedding models

**High API costs:**
- Monitor token usage and implement limits
- Cache responses for repeated queries
- Use smaller models for simple tasks

### Debug Mode
Enable detailed logging for troubleshooting:
```python
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

## Future Enhancements

### Planned Features
- Integration with actual order management systems
- Advanced analytics and reporting
- Voice interface support
- Mobile app integration
- Multi-tenant support for different businesses

### Technical Improvements
- Implement proper database backend
- Add comprehensive test suite
- Implement CI/CD pipeline
- Add performance monitoring
- Implement A/B testing for response quality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper testing
4. Submit a pull request with detailed description

## License

This project is licensed under the MIT License.

## Support

For technical support or questions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section above

## Acknowledgments

- AWS Bedrock for LLM capabilities
- Pinecone for vector database services
- Tavily for web search functionality
- The LangChain community for inspiration and best practices