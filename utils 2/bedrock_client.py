import boto3
import json
from config import Config    #from file name  import class name

def setup_bedrock():
    client = boto3.client(
        'bedrock-runtime',
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region_name=Config.AWS_REGION
    )
    return client

def call_claude(client, prompt, temperature=0.3, max_tokens=1024):
    payload = { 
               "anthropic_version": "bedrock-2023-05-31",
               "max_tokens": max_tokens,
               "temperature": temperature,
               "messages": [
                   {
                       "role": "user",
                       "content": prompt
                   }
               ]
    }
    
    try:
        response = client.invoke_model(
            modelId=Config.BEDROCK_MODEL_ID,
            body = json.dumps(payload).encode('utf-8'),
            contentType='application/json'
        )
        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']
    except Exception as e:
        print(f"Error calling Bedrock model: {e}")
        return None