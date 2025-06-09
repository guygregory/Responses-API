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
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input="Who was the wife of the president of the United States in 1960?",
    reasoning={
        "effort": "high",
        "summary": "auto" # auto, concise, or detailed (currently only supported with o4-mini and o3)
    }

)

# Parse and print only the summary text
for item in response.output:
    if getattr(item, "type", None) == "reasoning":
        for summary in getattr(item, "summary", []):
            print(summary.text)

print(response.output_text)
