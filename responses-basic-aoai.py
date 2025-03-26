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
    model=os.environ["AZURE_OPENAI_API_MODEL"], # replace with your model deployment name 
    input="This is a test."
    #truncation="auto" required when using computer-use-preview model.

)

print(response.output_text)