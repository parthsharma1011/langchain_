"""
Fact-checking system template with LangChain prompts
Add your real API keys to use this system
"""
import boto3
import json
from tavily import TavilyClient
from datetime import datetime
from typing import Dict, List, Optional
from prompts import get_fact_check_prompt

class Config:
    AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID_HERE'
    AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY_HERE'
    AWS_REGION = 'us-east-1'
    BEDROCK_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
    TAVILY_API_KEY = "YOUR_TAVILY_API_KEY_HERE"
    
def setup_bedrock_client():
    try:
        bedrock_client = boto3.client(
            service_name='bedrock-runtime',
            region_name=Config.AWS_REGION,
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
        )
        print("Bedrock client setup successfully.")
        return bedrock_client
    
    except Exception as e:
        print(f"Error setting up Bedrock client: {e}")
        return None
    
def call_bedrock(client, prompt, max_tokens=2000, temperature=0.7, top_p=0.95):
    payload = {
        "anthropic_version":"bedrock-2023-05-31",
        "max_tokens":max_tokens,
        "temperature":temperature,
        "top_p":top_p,
        "messages":[
            {
                "role":"user",
                "content":prompt
            }
        ]
    }
    
    try:
        response = client.invoke_model(
            modelId=Config.BEDROCK_MODEL_ID,
            body=json.dumps(payload).encode('utf-8'),
            contentType='application/json'
        )
        
        response_body = json.loads(response['body'].read().decode('utf-8'))
        return response_body['content'][0]['text']
    except Exception as e:
        print(f"Error calling Bedrock: {e}")
        
        
def search_evidence(tavily_client, claim):
    try:
        search_results = tavily_client.search(query=claim, 
                                              search_depth="advanced", 
                                              max_results=10)
        if not search_results.get("results"):
            print("No search results found.")
            return None, []
        
        evidence = ""
        sources = []
        
        for i, result in enumerate(search_results.get('results',[])[:5]):
            title = result.get('title', 'No Title Found! Sorry!')
            content = result.get('content', 'No Content Found! Sorry!')
            url = result.get('url', 'No URL Found! Sorry!')
            
            evidence += f"Source {i+1} Title: {title}\nContent: {content}\n\n"
            sources.append({
                "number": i+1,
                "title": title,
                "url": url,
                "snippet": content[:200]  # First 200 characters as snippet
            })
        return evidence, sources
    except Exception as e:
        print(f"Error searching evidence: {e}")
        return None, []
    
def fact_check(bedrock_client, tavily_client, claim):
    print(f"FACT CHECKING CLAIM: {claim}\n")
    evidence, sources = search_evidence(tavily_client, claim)
    if not evidence:
        return {
            "success": False,
            "error": "Failed to retrieve evidence., no search results found."
        }
    print(f"Found {len(sources)} sources. Generating fact-checking response...\n")
    
    prompt = get_fact_check_prompt(claim=claim, evidence=evidence)
    analysis = call_bedrock(bedrock_client,
                            prompt=prompt,
                            max_tokens=2000,
                            temperature=0.3,
                            top_p=0.9)
    
    if not analysis:
        return {
            "success": False,
            "error": "Failed to retrieve analysis."
        }
    
    return {
        "success": True,
        "claim": claim,
        "analysis": analysis,
        "sources": sources,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
def display_results(result):
    if not result.get("success"):
        print(f"Error: {result.get('error')}")
        return
    
    print(f"FACT-CHECK RESULTS:\n")
    print("=="*50)
    print(result['analysis'])
    
    print("\nSOURCES:")
    print("--"*50)
    for source in result['sources']:
        print(f"Source {source['number']}: {source['title']}")
        print(f"URL: {source['url']}")
        print(f"Snippet: {source['snippet']}\n")
    print("\n Completed at:", result['timestamp'])
    
def main():
    print(f"AWS BEDROCK + TAVILY FACT-CHECKER AGENT\n")
    print(f"="*60)
    bedrock_client = setup_bedrock_client()
    if not bedrock_client:
        print(f"Failed to initialize Bedrock client. Exiting.")
        return 
    tavily_client = TavilyClient(api_key=Config.TAVILY_API_KEY)
    print(f"Servies of tavily successfully initialized.")
    while True:
        try:
            claim = input("\nEnter a claim to fact-check (or type 'exit' to quit): ")
            if claim.lower() in ['exit', 'quit', 'q', 'close', 'stop', 'end']:
                print("Exiting Fact-Checker. Goodbye!")
                break
            if not claim:
                print("Please enter a valid claim.")
                continue
            result = fact_check(bedrock_client, tavily_client, claim)
            display_results(result)
        except KeyboardInterrupt:
            print("\nExiting Fact-Checker. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")
            
if __name__ == "__main__":
    main()