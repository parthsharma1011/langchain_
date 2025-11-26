"""
API Keys Configuration
All keys hardcoded for learning purposes
"""

# AWS Bedrock Credentials - REPLACE WITH YOUR KEYS
AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID_HERE'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY_HERE'
AWS_REGION = 'us-east-1'

# Alternative Bedrock API Key (Bearer token style) - REPLACE WITH YOUR KEY
BEDROCK_API_KEY = "YOUR_BEDROCK_API_KEY_HERE"

# Model IDs
ANTHROPIC_MODELS = {
    'haiku': 'anthropic.claude-3-haiku-20240307-v1:0',
    'sonnet': 'anthropic.claude-3-sonnet-20240229-v1:0',
    'opus': 'anthropic.claude-3-opus-20240229-v1:0'
}

AMAZON_MODELS = {
    'titan_text': 'amazon.titan-text-express-v1',
    'titan_embed': 'amazon.titan-embed-text-v1'
}

META_MODELS = {
    'llama2_13b': 'meta.llama2-13b-chat-v1',
    'llama2_70b': 'meta.llama2-70b-chat-v1'
}

COHERE_MODELS = {
    'command': 'cohere.command-text-v14',
    'command_light': 'cohere.command-light-text-v14'
}