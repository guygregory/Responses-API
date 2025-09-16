from openai import OpenAI 
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
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