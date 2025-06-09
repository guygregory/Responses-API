import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

response = client.responses.create(
    model="o4-mini",
    input="How much wood would a woodchuck chuck?",
    reasoning={
        "effort": "high"
    }
)

print(response.output_text)