import os
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(  
  base_url = os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),  
  api_key = token_provider
)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    tools=[
        {
            "type": "mcp",
            "server_label": "MicrosoftLearn",
            "server_url": "https://learn.microsoft.com/api/mcp",
            "allowed_tools": ["microsoft_docs_search", "microsoft_docs_search"],
            "require_approval": "never",
        },
    ],
    input="Provide a one-sentence summary of Azure AI Search, and provide a link to a Quickstart guide.",
)

print(response.output_text)

