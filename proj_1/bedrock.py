import boto3
import json
import base64
from typing import Dict, Any
from tavily import TavilyClient

# def setup_bedrock_client():
#     AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID_HERE'
#     AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY_HERE'
    
#     try:
#         bedrock_client = boto3.client(
#             service_name='bedrock-runtime',
#             region_name='us-east-1',
#             aws_access_key_id=AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=AWS_SECRET_ACCESS_KEY
#         )
#         print("Bedrock client setup successfully.")
#         return bedrock_client
    
#     except Exception as e:
#         print(f"Error setting up Bedrock client: {e}")
#         return None
    
# # bedrock_client = setup_bedrock_client()
# # print(bedrock_client)


# def basic_bedrock_call(client, prompt,model_id="anthropic.claude-3-haiku-20240307-v1:0"):
#     print(f"making a basic api call to. claude-3 haiku.")
#     if 'anthropic' in model_id:
#         payload = {
#             "anthropic_version":"bedrock-2023-05-31",
#             "max_tokens":1000,
#             "temperature":0.7,
#             "top_p":0.95,
#             "messages":[
#                 {
#                     "role":"user",
#                     "content":prompt
#                 }
#             ]
#         }
#     elif "meta.llama" in model_id:
#         payload = {
#             "prompt":prompt,
#             "max_tokens":1000,
#             "max_gen_len":1000,
#             "temperature":0.7,
#             "top_p":0.95,
#             "messages":[
#                 {
#                     "role":"user",
#                     "content":prompt
#                 }
#             ]
#         }
#     elif "amazon.titan" in model_id:
#         payload = {
#             "prompt":prompt,
#             "max_tokens":1000,
#             "temperature":0.7,
#             "top_p":0.95,
#             "messages":[
#                 {
#                     "role":"user",
#                     "content":prompt
#                 }
#             ]
#         }
        
#     try:
#         response = client.invoke_model(
#             modelId=model_id,
#             body = json.dumps(payload),
#             contentType='application/json',
#         )
#         response_body= json.loads(response['body'].read().decode('utf-8'))
#         # print('++-- Response Body --++')
#         # print(f"Full response: {response_body}")
#         # print('++-- end --++')
        
#         if "anthropic" in model_id:
#             text = response_body['content'][0]['text']
#         elif "meta.llama" in model_id:
#             text = response_body['genration']
#         elif "amazon.titan" in model_id:
#             text = response_body['results'][0]['outputText']
            
#         return text
            
#         print(f"Response from model: {text}")
#     except Exception as e:
#         print(f"Error during API call: {e}")
        
        
# client = setup_bedrock_client()
# call = basic_bedrock_call(client, "tell me about cors error in websites")
# print(f"Result: {call}")


#tavily how to use?
TAVILY_API_KEY = "YOUR_TAVILY_API_KEY_HERE"
tavily_client = TavilyClient(api_key = TAVILY_API_KEY)

#adavnced search. basic, advanced -> 
response = tavily_client.search(
    query="prime minister of india",
    search_depth= "advanced",
    max_results=5,
)

# print(f"response : {response}")
for result in response['results']:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['content']}")
    print("-----")

