class Config:
    
    #AWS BEDROCK CONFIGURATION
    AWS_ACCESS_KEY_ID = "your_aws_access_key_id"
    AWS_SECRET_ACCESS_KEY = "your_aws_secret_access_key"
    AWS_REGION = "us-east-1"
    BEDROCK_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
    
    #Tavily 
    TAVILY_API_KEY= "your_tavily_api_key"
    
    PINECONE_API_KEY = "your_pinecone_api_key"
    
    #AGENT SETTINGS
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7
    
    
    