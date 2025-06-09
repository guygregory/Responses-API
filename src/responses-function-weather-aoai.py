import requests
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for provided coordinates in celsius.",
    "parameters": {
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]

input_messages = [{"role": "user", "content": "What's the weather like in London today?"}]

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input=input_messages,
    tools=tools,
)

tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_weather(args["latitude"], args["longitude"])

input_messages.append(tool_call)  # append model's function call message
input_messages.append({                               # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)