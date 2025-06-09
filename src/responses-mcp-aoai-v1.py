import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
)

resp = client.responses.create(
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

print(resp.output_text)