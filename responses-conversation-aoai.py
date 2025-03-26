from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

previous_response_id = None

while True:
    user_input = input("Enter your message (or type 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        break

    if previous_response_id:
        response = client.responses.create(
            model=os.environ["AZURE_OPENAI_API_MODEL"],
            previous_response_id=previous_response_id,
            input=[{"role": "user", "content": user_input}],
        )
    else:
        response = client.responses.create(
            model=os.environ["AZURE_OPENAI_API_MODEL"],
            input=user_input,
        )

    print(response.output_text)
    previous_response_id = response.id