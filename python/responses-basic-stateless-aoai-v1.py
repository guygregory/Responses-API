import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input="Tell me a joke.",
    store=False, #store=false, to avoid storing sensitive data
    include=["reasoning.encrypted_content"] # Encrypted chain of thought is passed back in the response
)

print(response.output_text)