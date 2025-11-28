"""Agent:2
    search knowledge base (internal) -> this part of code can literally use anu information -> pdf, doc, db, sftp, anything
"""

import json 
from tavily import TavilyClient
from config import Config
from difflib import SequenceMatcher
from pinecone import Pinecone
import time
import hashlib 

class InformationRetrieverAgent:
    def __init__(self, bedrock_client):
        self.client = bedrock_client
        self.name = "Information Retriever"
        self.tavily = TavilyClient(api_key=Config.TAVILY_API_KEY)
        
        #load local knowledge base
        with open('data/support_guide.txt','r') as f:
            self.knowledge_base = f.read()
            
        with open('data/orders.json','r') as f:
            orders_data = json.load(f)
            self.orders_db = orders_data.get('orders', [])
            
        # Initialize simple text search
        self.kb_chunks = self._prepare_knowledge_chunks()
        
        # Initialize Pinecone vector database
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
    
    def _prepare_knowledge_chunks(self):
        chunks = self.knowledge_base.split('\n\n')
        return [chunk.strip() for chunk in chunks if chunk.strip()]
    
    def _setup_pinecone(self):
        try:
            pc = Pinecone(api_key=Config.PINECONE_API_KEY)
            index_name = "knowledge-base"
            
            #create index if it doesn't exist
            if index_name not in pc.list_indexes().names():
                pc.create_index(
                    name=index_name,
                    dimension=384,
                    metric='cosine',
                    spec = {'serverless':
                        {"cloud":"aws",
                         "region":"us-east-1"}}
                )
                time.sleep(10)
                
            self.index = pc.Index(index_name)
            
            embeddings = self._create_simple_embeddings()
            
            vectors = [
                {
                    "id": f"chunk_{i}",
                    "values": embeddings[i],
                    "metadata": {"text":chunk}
                }
                for i, chunk in enumerate(self.kb_chunks)
            ]
            
            self.index.upsert(vectors=vectors)
        except Exception as e:
            print(f"Error setting up Pinecone: {e}")
            self.index = None
           
    #not very good technique 
    def _create_simple_embeddings(self):
        embeddings = []
        vocab = set() # no order 
        
        for chunk in self.kb_chunks:
            words = chunk.lower().split()
            vocab.update(words)
        
        vocab = list(vocab)[:384]
        
        #create embeddings for each chunk
        for chunk in self.kb_chunks:
            words = chunk.lower().split()
            embedding = [0.0] * 384
            
            for i, word in enumerate(vocab):
                if i < 384:
                    embedding[i] = word.count(word) / len(words) if words else 0.0  
                    
            embeddings.append(embedding)    
        return embeddings
    
    def _create_query_embedding(self, query):
        vocab = set()
        for chunk in self.kb_chunks:
            vocab.update(chunk.lower().split())
        vocab = list(vocab)[:384]
        
        #create a query emb
        query_words = query.lower().split()
        embedding = [0.0] * 384
        
        for i, word in enumerate(vocab):
                if i < 384:
                    embedding[i] = query_words.count(word) / len(query_words) if query_words else 0.0
        return embedding
    
    def _search_orders(self,order_id):
        for order in self.orders_db:
            if order.get('order_id', '').lower() == order_id.lower():
                return f"Order {order['order_id']}: Status - {order['status']}, Items - {', '.join(order['items'])}, Total - Euro{order['total']}, Tracking - {order['tracking']}"
        return None
    
    def _search_orders_by_customer(self, customer_info):
        results = []
        for order in self.orders_db:
            if (customer_info.lower() in order.get('customer_email','').lower() or 
                customer_info.lower() in order.get('customer_name', '').lower()):
                results.append(f"Order {order['order_id']}: Status - {order['status']}, Items - {', '.join(order['items'])}, Total - Euro{order['total']}, Tracking - {order['tracking']}")
        return '\n'.join(results) if results else None
    
    def _search_knowledge_base(self, query):
        try:
            if not self.index:
                return self._fallback_text_search(query)
            
            query_embedding = self._create_query_embedding(query)
            
            results = self.index.query(
                vector=query_embedding,
                top_k=3,
                include_metadata=True
            )
            
            #chunk - text 
            if results.matches:
                return '\n'.join(match.metadata['text'] for match in results.matches)
        except Exception as e:
            print(f"Error searching knowledge base: {e}")
            return self._fallback_text_search(query)
        return None
    
    def _fallback_text_search(self, query):
        try:
            query_lower = query.lower()
            best_matches = []
            
            for chunk in self.kb_chunks:
                chunk_lower = chunk.lower()
                if any(word in chunk_lower for word in query_lower.split() if len(word) > 2):
                    similarity = SequenceMatcher(None, query_lower, chunk_lower).ratio()
                    best_matches.append((similarity, chunk))
                    
            best_matches.sort(key=lambda x: x[0], reverse=True)
            if best_matches:
                return "\n".join(match[1] for match in best_matches[:3])
        except Exception as e:
            print(f"Error in fallback text search: {e}")
        return None
    
    def _web_search(self, query):
        try:
            response=self.tavily.search(query=query, search_depth='advanced', max_results=3)
            if response and 'results' in response:
                results = []
                for result in response['results']:
                    results.append(f"Title: {result['title']}\nContent: {result['content']}")
                return '\n'.join(results)
        except Exception as e:
            print(f"Web search error : {str(e)}")
        return None
            