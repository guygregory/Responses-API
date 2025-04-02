from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv
import os
import gradio as gr
import base64

# Load configuration settings from a .env file
load_dotenv()

# Set the AI host to Azure, OpenAI, or GitHub Models (coming soon)
AIhost = "AzureOpenAI" # set to "AzureOpenAI", "OpenAI", or "GitHub" based on your requirement

def get_client(host: str):
    """
    Returns the deployment and client based on the specified host.
    Exits the application if an unsupported host is provided.
    """
    if host == "AzureOpenAI":
        deployment = os.environ["AZURE_OPENAI_API_MODEL"]
        client = AzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_API_ENDPOINT"]
        )
    elif host == "OpenAI":
        deployment = "gpt-4o-mini"
        client = OpenAI()
    elif host == "GitHub":
        deployment = "gpt-4o-mini"
        print("GitHub Models are not yet supported in this demo. Please check back later.")
        exit(0)
    else:
        print("Invalid AI host specified. Please set AIhost to 'AzureOpenAI', 'OpenAI', or 'GitHub', and provide the configuration in the .env file")
        exit(0)
    return deployment, client

# Set the AI host to Azure, OpenAI, or GitHub Models (coming soon)
deployment, client = get_client(AIhost)

# Global variable to store the response identifier from the last API call
previous_response_id = None

def encode_image(image_path):
    """
    Opens the specified image file, encodes it in base64, and returns the encoded string.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def chat_stream(user_prompt, history, file_path):
    """
    Handles a chat interaction by:
    1. Adding the user's message to the conversation history.
    2. Creating a placeholder for the assistant's reply.
    3. Beginning a streamed API call to get the response.
    4. Appending streamed chunks to the assistant's message and yielding updates.
    
    If an image file is provided via file_path, it will be encoded and sent along with the user's input.
    """
    # Ensure the history list is initialized
    if history is None:
        history = []
    
    # Add the user prompt to the conversation history with appropriate role
    history.append({"role": "user", "content": user_prompt})
    
    # Create and add a placeholder for the assistant's reply
    assistant_message = {"role": "assistant", "content": ""}
    history.append(assistant_message)
    
    # Yield initial state to update the UI
    yield history, history

    # Prepare parameters for the API call, including model name and streaming flag
    global previous_response_id
    params = {
        "model": deployment,
        "input": [{"role": "user", "content": user_prompt}],
        "stream": True
    }
    
    # Attach the previous response ID for context if available
    if previous_response_id:
        params["previous_response_id"] = previous_response_id

    # If an image file was uploaded, encode it to base64 and add it to the input payload
    if file_path is not None:
        base64_image = encode_image(file_path)
        params["input"].append({
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}"
                }
            ]
        })

    # Initiate the streaming conversation using the client
    stream = client.responses.create(**params)
    
    # Process each event from the stream to build the complete assistant message
    for event in stream:
        # Record the response id from the first event
        if event.type == 'response.created':
            previous_response_id = event.response.id
            
        # Append new text received in the stream to the assistant message
        if event.type == 'response.output_text.delta':
            assistant_message["content"] += event.delta
            yield history, history

def clear_chat():
    """
    Resets the conversation state by clearing the chat history, previous response identifier,
    and the file upload.
    """
    global previous_response_id
    previous_response_id = None
    return [], [], None

# Clears the textbox input
def clear_textbox():
    return ""

# Build the Gradio Blocks interface for the chat demo
with gr.Blocks() as demo:
    # Header Markdown text for the demo UI, centered
    gr.Markdown("<h2 style='text-align: center;'>Responses API Demo</h2>")
    
    # Chatbot component to display messages stored in a list of role-content dictionaries
    chatbot = gr.Chatbot(height=500, type="messages")
    
    # State to maintain the conversation history between messages
    state = gr.State([])
    
    # Textbox for user input with a placeholder message
    msg = gr.Textbox(show_label=False, placeholder="Type your message here and press Enter")
    
    # Row containing the Submit and Clear buttons
    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")
    
    # File upload control for image inputs (placed below the buttons)
    file_picker = gr.File(label="Upload an Image", file_count="single", type="filepath", file_types=[".jpg", ".jpeg", ".png"], height=140)
    
    # Bind the Textbox submit action to the stream processing function and clear the textbox after submission
    msg.submit(fn=chat_stream, inputs=[msg, state, file_picker], outputs=[chatbot, state]).then(
        clear_textbox, None, msg
    )
    
    # Also bind the submit button to the same functionality as the Textbox submit
    submit_btn.click(fn=chat_stream, inputs=[msg, state, file_picker], outputs=[chatbot, state]).then(
        clear_textbox, None, msg
    )
    
    # Bind the clear button to reset the chat and clear the file upload
    clear_btn.click(fn=clear_chat, inputs=[], outputs=[chatbot, state, file_picker])

# Launch the Gradio demo application
demo.launch()
