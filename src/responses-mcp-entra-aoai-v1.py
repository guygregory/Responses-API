import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(  
  base_url = os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),  
  azure_ad_token_provider=token_provider,
  api_version="preview"
)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    tools=[
        {
            "type": "mcp",
            "server_label": "cloudflare",
            "server_url": "https://docs.mcp.cloudflare.com/sse",
            "require_approval": "never",
        },
    ],
    input="Do Cloudflare Workers costs depend on response sizes? I want to serve some images (map tiles) from an R2 bucket and I'm concerned about costs.",
)

print(response.output_text)