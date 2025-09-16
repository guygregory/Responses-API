from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
)

# Upload a file with a purpose of "assistants"
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