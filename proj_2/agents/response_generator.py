"""
Agent:3
Compose a final customer response based on gathered information
"""

from utils.bedrock_client import call_claude

class ResponseGeneratorAgent:
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client
        self.name = "Response Generator"
        
    def generate(self, query_analysis, retrieved_info):
        """Genertae final customer response

        Args:
            query_analysis : Dict from QueryAnalyzerAgent
            retrieved_info : Dict from Information_ret Agent
        Return:
        final respoinse. : Str
        """
        print(f"    [{self.name}] Generating Response...")
        original_query = query_analysis['original_query']
        information = retrieved_info['information']
        sources = retrieved_info['sources']
        urgency = query_analysis['urgency']
        missing_info = query_analysis.get('missing_info','none')
        query_type = query_analysis['query_type']
        
        if "MISSING_INFORMATION" in information:
            prompt = f"""
            You are a friendly customer service agent for Asia on Plate, an Asian grocery delivery service in Berlin.
            
            CUSTOMER QUERY: "{original_query}"
            QUERY TYPE: {query_type}
            MISSING INFORMATION : {missing_info}
            
            The customer's query cannot be fully processed because important information is missing.
            
            Generate a polite response that:
            1. Acknowledges their request
            2. Explain what specific information you need to help them
            3. Asks for the missing details in a friendly way
            4. Maintain a warm, professional tone
            5. Respond ONLY in English if query in English, German if query in German
            
            For order tracking: Ask for order ID OR (customer email + full name)
            For returns/redunds: Ask for order ID or (customer email + full name) + reason for return
            For account issues: Ask for customer email OR full name
            
            Write a helful response asking for the missing information:"""
        else:
            prompt = f"""
            You are a friendly customer service agent for Asia on Plate, an Asian grocery delivery service in Berlin.
            
            CUSTOMER QUERY: "{original_query}"
            AVAILABLE INFORMATION : {information}
            URGENCY: {urgency}
            
            Generate a helpful, friendly response that:
            1. Directly answers, the customer's question using the information provided
            2. Maintains a warm,professional tone
            3. Keep it concise but complete
            4. If urgent, acknowledge the urgency
            5. Respond ONLY in English if query in English, German if query in German
            6. Ends with asking if they need any additional help.
            
            IMPORTANT RULES:
            - Never mention "sources", "information retrieval", or "database"
            - Write naturally as a human customer service agent
            - Be specific and helpful with the information provided
            - If no relevant information was found, politely explain and offer alternatives
            
            Write the response now:"""
            
            
            
            
            
            
            
            
