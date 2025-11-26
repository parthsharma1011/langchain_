# import google.generativeai as genai
# genai.configure(api_key="AIzaSyDG3btOmGFFQM1h3G_ia2xNcvk1YxXWVsU")
# available_models = genai.list_models()
# print(list(available_models))

# from langchain_google_genai import ChatGoogleGenerativeAI
# # genai.configure(api_key="AIzaSyDG3btOmGFFQM1h3G_ia2xNcvk1YxXWVsU")

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     google_api_key = "AIzaSyDG3btOmGFFQM1h3G_ia2xNcvk1YxXWVsU",
#     temperature=0.7,
#     max_output_tokens=1000
# )
# response = llm.invoke("explain machine learning in one sentence")
# print(response)

# #creating a react agent with google gemini
# import google.generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.schema import HumanMessage, AIMessage
# import re 

# gemini_api_key = "AIzaSyDG3btOmGFFQM1h3G_ia2xNcvk1YxXWVsU" #never hardcod
# genai.configure(api_key=gemini_api_key)

# #initliase llm
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     google_api_key = gemini_api_key,
#     temperature=0.7,
#     max_output_tokens=512
# )

# #before you build any agent u need to define tools
# def calculate(expression):
#     return eval(expression) #testing only, never use eval in production code

# def average_pill_weight(name):
#     pill_weights = {
#         "aspirin": "500 mg",
#         "ibuprofen": "650 mg",
#         "acetaminophen": "400 mg"
#     }
#     return f"The average weight of {name} is {pill_weights.get(name.lower(), 'unknown')}."

# known_actions = {
#     "calculate": calculate,
#     "average_pill_weight": average_pill_weight
# }

# class Agent:
#     def __init__(self):
#         self.messages = [] #memory layer, simple implementation
        
#     def __call__(self,message):
#         self.messages.append(HumanMessage(content=message)) #this is user input
#         response = self.execute()
#         self.messages.append(AIMessage(content=response)) #this is agent response
#         return response
        
#     def execute(self):
#         response = llm.invoke(self.messages)
#         return response.content 
    
# #once the code is over 
# action_re = re.compile(r'Action:\s*(\w+):\s*(.*?)(?:\n|$)',re.MULTILINE)

# def run_query(prompt, max_turns=10):
#     agent = Agent()
#     next_prompt = prompt 
#     for turn in range(max_turns):
#         print(f"Turn: {turn+1}")
#         response = agent(next_prompt)
#         print(f"Assistant: \n{response}\n")
        
#         actions= action_re.findall(response)
        
#         if actions:
#             action, action_input = actions[0]
#             action_input = action_input.strip()
            
#             if action not in known_actions:
#                 raise ValueError(f"Unknown action: {action}")
            
#             observation = known_actions[action](action_input)
#             print(f"Observation: {observation}\n")
#             next_prompt = f"Observation: {observation}\n"
#         else:
#             if "Answer:" in response:
#                 print("Final Answer found. Ending interaction.")
#                 break
#             else:
#                 print("No action found and no final answer. Ending interaction.")
#                 break
#     return agent
            
# instruction_and_questions = """
# You are a helpful assisatnt following a React reasoning pattern.

# for each step:
# 1. Use 'Thought:' to think step by step about the problem.
# 2. If you need more information, use 'Action: <action_name>: <action_input>' on a new line
# 3. After each action, I will provide an 'Observation: <observation>' on a new line with the result of the action.
# 4. Continue thinking and acting until you reach a final answer.  'Answer: <final_answer>' on a new line.

# Available actions:
# - calculate: to perform mathematical calculations. Input should be a valid mathematical expression.
# - average_pill_weight: to get the average weight of a pill. Input should be the name of the pill.   

# Important : Only perform ONE action at a time, then wait for the observation before proceeding.
# Here is the question:
# I have two pills, aspirin and acetaminophen? what is their combined weight
# """

# agent = run_query(instruction_and_questions, max_turns=5)
# print("Final Answer:")
# print(agent.messages[-1].content if agent.messages else "No messages")
# print("=="*30)
# print(f"MESSAGES: {agent.messages}")
# print("=="*30)
        
        




