# Uses async client to continuously stream data from the server to the client.
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
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