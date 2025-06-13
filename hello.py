
import os  
from dotenv import load_dotenv  
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

load_dotenv() 
my_api_key = os.getenv("GEMINI_API_KEY")  


if not my_api_key:
    raise ValueError("GEMINI_API_KEY is not set.") 

external_client = AsyncOpenAI(
    api_key=my_api_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  
    openai_client=external_client  
)

config = RunConfig(
    model=model,  
    model_provider=external_client,  
    tracing_disabled=True 
)

myAgent = Agent(
    name="InfoBuddy",
    instructions=(
        "You are a friendly, knowledgeable assistant. "
        "Give clear, brief responses and break down concepts into simple, understandable terms."
    ),  
    model=model 
)


print("Hello and welcome to InfoBuddy! Enter 'exit' to close the chat.")  

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! See you next time!")
        break  

  
    response = Runner.run_sync(myAgent, user_input, run_config=config)
    print(f"QueryBot: {response.final_output}")