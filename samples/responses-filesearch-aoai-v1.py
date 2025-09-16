import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
)

# Create a vector store in Azure OpenAI
vector_store = client.vector_stores.create(
    name="Employee Handbook"
)

# Ready the files for upload to Azure OpenAI
file_paths = ["../assets/employee_handbook.pdf"]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# Optional - print the upload status, file counts, and vector store ID
# # print(file_batch.status)
# print(file_batch.file_counts)
# print("Vector Store ID:",vector_store.id)

# Query the vector store
response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    tools=[{
      "type": "file_search",
      "vector_store_ids": [vector_store.id],
      "max_num_results": 20
    }],
    input="What are the company values?",
)

print(response.output_text)

# Delete the vector store
client.vector_stores.delete(vector_store_id=vector_store.id)