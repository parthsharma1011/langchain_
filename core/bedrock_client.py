"""
Core Bedrock Client Setup
"""
import boto3
import json
from config.api_keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

def setup_bedrock_client():
    """Setup AWS Bedrock client with credentials"""
    try:
        client = boto3.client(
            service_name='bedrock-runtime',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        print("✅ Bedrock client setup successfully")
        return client
    except Exception as e:
        print(f"❌ Error setting up Bedrock client: {e}")
        return None

def invoke_model(client, model_id, payload):
    """Generic model invocation"""
    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(payload),
            contentType='application/json'
        )
        return json.loads(response['body'].read().decode('utf-8'))
    except Exception as e:
        print(f"❌ Error invoking model: {e}")
        return None