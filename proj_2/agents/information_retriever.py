"""Agent:2
    search knowledge base (internal) -> this part of code can literally use anu information -> pdf, doc, db, sftp, anything
"""

import json 
from tavily import TavilyClient
from config import Config

#Vector db -> 

class InformationRetrieverAgent:
    def __init__(self, bedrock_client):
        self.client = bedrock_client
        self.name = "Information Retriever"
        self.tavily = TavilyClient(api_key=Config.TAVILY_API_KEY)
        
        #load local knowledge base
        with open('data/support_guide.txt','r') as f:
            self.knowledge_base = f.read()
            
        with open('data/orders_json','r') as f:
            self.orders_db = json.load(f)
            
        self.kb_chunks = self._prepare_knowledge_chunks()
        
        self._setup_pinecone()
            
    def retrieve(self,query_analysis):
        """
        Retreive relevant information based on query analysis

        Args:
            query_analysis : Dict from QueryAnalyzerAgent

        Returns:
            Dict with sources and information
        """
        print(f"\n [{self.name}] Retrieving information...")
        
        query_type = query_analysis['query_type']
        key_info = query_analysis['key_info']
        missing_info = query_analysis.get('missing_info', 'none')
        needs_search = query_analysis['needs_search']
        
        result = {
            'sources':[],
            'information': '',
            'method':'',
            'missing_info': missing_info
        }
        
        if query_type == 'order_tracking':
            if key_info != 'none':
                #first try order ID lookup
                order_info = self._search_orders(key_info)
                if order_info:
                    result['sources'].append("Internal Order Database")
                    result['information'] = order_info
                    result['method'] = 'order_lookup'
                    print(f"    Found order information")
                    return result
                
                # if no order ID is found, try customer lookup
                customer_info = self._search_orders_by_customer(key_info)
                if customer_info:
                    result['sources'].append("Internal Order Database")
                    result['information'] = customer_info
                    result['method'] = 'customer_lookup'
                    print(f"    Found customer orders")
                    return result
                
            search_terms = [query_analysis['original_query']]
            if key_info != 'none':
                search_terms.append(key_info)
                
            for search_term in search_terms:
                customer_info = self._search_orders_by_customer(search_term)
                if customer_info:
                    result['sources'].append("Internal Order Database")
                    result['information'] = customer_info
                    result['method'] = 'customer_lookup'
                    print(f"    Found customer orders")
                    return result
                
        #if critical info is missing, and no orders found, note it.        
        if missing_info != 'none' and query_type == 'order_tracking':
            result['information'] = f"MISSING_INFORMATION: {missing_info}\n\n"
            print(f"    Missing : {missing_info}")
            
        #search local knowledge base
        kb_info = self._search_knowledge_base(query_analysis['original_query'])
        if kb_info:
            result['sources'].append("Internal Knowledge Base")
            result['information'] += kb_info + '\n\n'
            result['method'] = 'knowledge_base'
            print(f"    Found information in Knowledge Base")
            
        #if needs web search. use Tavily
        if needs_search:
            web_info = self._web_search(query_analysis['original_query'])
            if web_info:
                result['sources'].append("Web Search (Tavily)")
                result['information'] += web_info + '\n\n'
                result['method'] = 'web_search'
                print(f"    Found information in Web Search")
                
        if not result['information'] or (result['information'].strip() == f"MISSING_INFORMATION: {missing_info}\n\n" if missing_info != 'none' else False):
            if query_type == 'order_tracking':
                result['information'] = "No specific order information found in our records."
            else:
                result['information'] = "No relevant information found in our records."
            print(f"    No information found")
            
        return result
            
        
        
                
             
        
        
        
        
        
        

    
    