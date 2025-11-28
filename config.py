import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    
    #AWS BEDROCK CONFIGURATION
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "your_aws_access_key_id")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your_aws_secret_access_key")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")
    
    #Tavily 
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "your_tavily_api_key")
    
    #Pinecone
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "your_pinecone_api_key")
    
    #AGENT SETTINGS
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
