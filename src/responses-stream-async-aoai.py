# Uses async client to continuously stream data from the server to the client.
from openai import AsyncAzureOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

client = AsyncAzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

async def main():
    stream = await client.responses.create(
        model=os.environ["AZURE_OPENAI_API_MODEL"],
        input="Write me a poem about the sea.",
        stream=True,
    )

    async for event in stream:
        if hasattr(event, "delta") and event.delta:
            print(event.delta, end="", flush=True)

asyncio.run(main())