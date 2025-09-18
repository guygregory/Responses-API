from openai import AzureOpenAI
from dotenv import load_dotenv
import base64
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    base_url=os.getenv("AZURE_OPENAI_V1_API_IMAGE_ENDPOINT"),
    azure_ad_token_provider=token_provider,
    default_headers={"x-ms-oai-image-generation-deployment":"gpt-image-1"}
)

response = client.responses.create(
    model="gpt-4o",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))