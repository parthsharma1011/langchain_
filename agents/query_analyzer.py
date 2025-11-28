"""Agent:1 Query Analyzer
Analyzes user queries to determine their intent and required actions.
"""

from utils.bedrock_client import call_claude

class QueryAnalyzerAgent:
    """First agent in the chain of operation, 
    it determines the query type and extracts key information"""
    
    def __init__(self, bedrock_client):
        self.client = bedrock_client
        self.name = "QueryAnalyzer"
        
    def analyze(self, customer_query):
        print(f"\n [{self.name}] Analyzing customer query...")
        prompt = f"""You are a customer service query analyzer for Asia on Plate (name of the b2b retail company in germany),
        Analyze this customer query and respond ONLY in English if the user query is in English,
        else if user query is in German respond ONLY in German. English and German are the only languages you can respond in.
        
    QUERY : "{customer_query}"
    
    Determine:
    1) Query Type: Choose ONE from [order_tracking, product_info, delivery_info, return_refund, general_questions, account_issue]
    2) Key Information: Extract order ID's, product names, email addresses, or important details.
    3) Missing Information: What essential info is missing for this query type?
    4) Needs Search: Does this need web search? (yes/no)
    5) Urgency: low/medium/high 
    
    For order tracking queries, we need: order ID OR (customer email + name)
    For returns/refund, we need: order ID OR (customer email + name) + reason
    for account issues, we need: customer email or name 
    
    Respond in this EXACT FORMAT:
    QUERY_TYPE = [type]
    KEY_INFO: [extracted info or "none"]
    MISSING_INFO:[whats missing or "none"]
    NEEDS_SEARCH:[yes/no]
    URGENCY:[low/medium/high]
        Example:
        QUERY_TYPE = order_tracking
        KEY_INFO = 123456
        MISSING_INFO = none
        NEEDS_SEARCH = no
        URGENCY = low
    REASONING = [brief 1-sentence explanation]
    
    IMPORTANT: Respond only in English and german only if the user query asked is in english or german
    """
        response = call_claude(self.client, prompt, temperature=0.2, max_tokens=4000)
        if not response:
            return None
        result = self._parse_response(response, customer_query)
        
        print(f"    TYPE: {result['query_type']}']")
        print(f"    KEY INFO: {result['key_info']}']")
        print(f"    MISSING INFO: {result['missing_info']}']")
        print(f"    NEEDS SEARCH: {result['needs_search']}']")
        print(f"    URGENCY: {result['urgency']}']")
        
        return result
    
    def _parse_response(self, response,original_query):
        lines = response.strip().split('\n')
        result = {
            'original_query': original_query,
            'query_type': 'general_question',
            'key_info': 'None',
            'missing_info': 'None',
            'needs_search': False,
            'urgency': 'medium',
            'reasoning': ''
        }
        
        #i am not a big fan if-else, nested if-else dict
        for line in lines:
            line = line.strip()
            if "QUERY_TYPE" in line:
                if "=" in line:
                    result['query_type'] = line.split("=", 1)[1].strip().lower()
                elif ":" in line:
                    result['query_type'] = line.split(":", 1)[1].strip().lower()
            elif "KEY_INFO" in line:
                if "=" in line:
                    result['key_info'] = line.split("=", 1)[1].strip()
                elif ":" in line:
                    result['key_info'] = line.split(":", 1)[1].strip()
            elif "MISSING_INFO" in line:
                if "=" in line:
                    result['missing_info'] = line.split("=", 1)[1].strip()
                elif ":" in line:
                    result['missing_info'] = line.split(":", 1)[1].strip()
            elif "NEEDS_SEARCH" in line:
                result['needs_search'] = 'yes' in line.lower()
            elif "URGENCY" in line:
                if "=" in line:
                    result['urgency'] = line.split("=", 1)[1].strip().lower()
                elif ":" in line:
                    result['urgency'] = line.split(":", 1)[1].strip().lower()
            elif "REASONING" in line:
                if "=" in line:
                    result['reasoning'] = line.split("=", 1)[1].strip()
                elif ":" in line:
                    result['reasoning'] = line.split(":", 1)[1].strip()
        return result
            
        
        
           
#tools selection criterria -> pricing, scalability, ease of use, skill-gap
# - pricing, pay-as-you go, bulk load (40 gb), 
# - scalablity -> vertical, hor,
# ease of use -> tool, famolity (AWS), 
# SKILLS -> gaps (how long, how confi )
# p> s > e >s

# 5$ -> free,          render - free 4cpu
# more                    LESS
# NOT VERY EASY.       EASY, NO SKILS SIMPLE
# (REG SCRIPT)

# MEDIUM/HIGH.           LOW

