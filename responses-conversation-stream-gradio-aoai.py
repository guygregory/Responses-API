from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import gradio as gr

load_dotenv()

client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_API_ENDPOINT"]
)

previous_response_id = None

def chat_stream(user_prompt, history):
    # Ensure history is a list.
    if history is None:
        history = []
    # Append the user's message in the correct dictionary format.
    history.append({"role": "user", "content": user_prompt})
    # Create a placeholder for the assistant's response.
    assistant_message = {"role": "assistant", "content": ""}
    history.append(assistant_message)
    # Yield the initial conversation state.
    yield history, history

    global previous_response_id
    params = {
        "model": os.environ["AZURE_OPENAI_API_MODEL"],
        "input": [{"role": "user", "content": user_prompt}],
        "stream": True
    }
    if previous_response_id:
        params["previous_response_id"] = previous_response_id

    stream = client.responses.create(**params)
    
    # Update the assistant's message with the streamed response.
    for event in stream:
        if event.type == 'response.created':
            previous_response_id = event.response.id
        if event.type == 'response.output_text.delta':
            assistant_message["content"] += event.delta
            yield history, history

def clear_chat():
    global previous_response_id
    previous_response_id = None
    return [], []

def clear_textbox():
    return ""

with gr.Blocks() as demo:
    gr.Markdown("## Responses API on Azure OpenAI Streaming Demo")
    # Specify type="messages" so that each message is a dictionary with 'role' and 'content'
    chatbot = gr.Chatbot(height=500, type="messages")
    state = gr.State([])
    msg = gr.Textbox(show_label=False, placeholder="Type your message here and press Enter")
    
    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")
    
    msg.submit(fn=chat_stream, inputs=[msg, state], outputs=[chatbot, state]).then(
        clear_textbox, None, msg
    )
    submit_btn.click(fn=chat_stream, inputs=[msg, state], outputs=[chatbot, state]).then(
        clear_textbox, None, msg
    )
    clear_btn.click(fn=clear_chat, inputs=[], outputs=[chatbot, state])

demo.launch()
