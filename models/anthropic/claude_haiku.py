"""
Claude Haiku Model Implementation
Fast and efficient for simple tasks
"""
from core.bedrock_client import setup_bedrock_client, invoke_model
from config.api_keys import ANTHROPIC_MODELS

class ClaudeHaiku:
    def __init__(self):
        self.client = setup_bedrock_client()
        self.model_id = ANTHROPIC_MODELS['haiku']
    
    def chat(self, prompt, max_tokens=1000, temperature=0.7):
        """Send message to Claude Haiku"""
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = invoke_model(self.client, self.model_id, payload)
        if response:
            return response['content'][0]['text']
        return None

# Quick test
if __name__ == "__main__":
    haiku = ClaudeHaiku()
    result = haiku.chat("Hello! Introduce yourself in one sentence.")
    print(f"🤖 Haiku: {result}")