from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
from dotenv import load_dotenv
load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(  
  base_url = os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
  azure_ad_token_provider=token_provider,
)

# Upload a file with a purpose of "batch"
file = client.files.create(
  file=open("../assets/employee_handbook.pdf", "rb"), # This assumes a .pdf file in the assets directory
  purpose="assistants"
)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id":file.id
                },
                {
                    "type": "input_text",
                    "text": "What are the company values?",
                },
            ],
        },
    ]
)

print(response.output_text)