from utils.bedrock_client import setup_bedrock
from agents.query_analyzer import QueryAnalyzerAgent
from agents.information_retriever import InformationRetrieverAgent
from agents.response_generator import ResponseGeneratorAgent

class AsiaonPlateBot:
    def __init__(self):
        print(f"Initializing Asia on Plate Customer Service Bot.....")
        
        self.bedrock_client = setup_bedrock()
        self.query_analyzer = QueryAnalyzerAgent(self.bedrock_client)
        self.information_retriever = InformationRetrieverAgent(self.bedrock_client)
        self.response_generator = ResponseGeneratorAgent(self.bedrock_client)
        
        #conversation memory - tracks ongoing conversations
        # cust - i want to track my order
        # bot: pleas provide yournorder id or email
        #cust - parth@abc.com -> 
        self.conversation_state = {
            "waiting_for":None,  #what info am i waiting for?
            "original_query":None, #the cust og question 
            "query_type":None #type of query
        }
        
        print(f"Bot initialized successfully!")
        
    def process_query(self, customer_query):
        print(f"Processing : {customer_query}")
        
        if self.conversation_state['waiting_for']:
            return self._handle_followup(customer_query)
        
        #STEP : QUERY ANALYIS
        analysis = self.query_analyzer.analyze(customer_query)
        if not analysis:
            return "I apologize, but I'm having trouble processing your request right now. Please try again."
        
        #step -2 INFORMATION RE
        info = self.information_retriever.retrieve(analysis)
        
        #step 3 manage comverdation 
        if "MISSING_INFORMATION" in info.get("information",''):
            self.conversation_state = {
                'waiting_for':'customer_info' if analysis['query_type'] == 'order_tracking' else 'additional_info',
                'original_query':customer_query,
                'query_type':analysis['query_type']
            }
        response = self.response_generator.generate(analysis, info)
        return response
    
    def _handle_followup(self,customer_input):
        print(f"Processing followup information")
        if self.conversation_state['query_type'] == 'order_tracking':
            combined_query = f"{self.conversation_state['original_query']} {customer_input}"
            
            analysis = {
                'original_query':combined_query,
                'query_type':'order_tracking',
                'key_info':customer_input.strip(),
                'missing_info':'none',
                'needs_search':False,
                'urgency':'medium'
            }
            
            info = self.information_retriever.retrieve(analysis)
            
            self.conversation_state = {
                'waiting_for':None,
                'original_query':None,
                'query_type':None
            }
            
            response = self.response_generator.generate(analysis, info)
            return response
        
        self.conversation_state = {
            "waiting_for":None,
            "original_query":None,
            "query_type":None
        }
        return self.process_query(customer_input)
    
    def run_interactive(self):
        print(f"Asia on plate Customer Service Bot.....")
        print(f"Type 'quit' to exit\n")
        
        while True:
            try:
                query = input("Customer: ").strip()
                
                if query.lower() in ['quit','exit','bye']:
                    print("Thank you for using Asia on Plate bot.....")
                    break
                    
                if query:
                    response = self.process_query(query)
                    print(f"\nBot: {response}\n")
                    print("--------------------------------------------------\n")
            except KeyboardInterrupt:
                print("\nThank you for using Asia on Plate bot.....")
                break
            except Exception as e:
                print(f"An error occured: {e}")
                
def main():
    try:
        bot = AsiaonPlateBot()
        bot.run_interactive()
    except Exception as e:
        print(f"An error occured: {e}")
        
        
if __name__ == "__main__":
    main()

        
        
    