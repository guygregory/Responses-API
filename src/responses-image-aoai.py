from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

IMAGE_PATH = "./book.jpeg"

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image(IMAGE_PATH)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input=[
        {"role": "user", "content": "Identify the bird on the front of this book cover."},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}"
                }
            ]
        }
    ]
)

print(response.output_text)