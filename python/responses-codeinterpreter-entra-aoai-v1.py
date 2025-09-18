from openai import AzureOpenAI 
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
import os
load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(  
  base_url = os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),  
  azure_ad_token_provider=token_provider,
)

instructions = "You are a personal math tutor. When asked a math question, write and run code using the python tool to answer the question."

response = client.responses.create(
    model = os.getenv("AZURE_OPENAI_API_MODEL"), 
    tools = [
        {
            "type": "code_interpreter",
            "container": {"type": "auto"}
        }
    ],
    instructions=instructions,
    input="I need to solve the equation 3x + 11 = 14. Can you help me?",
)

print(response.output)