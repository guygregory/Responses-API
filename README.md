# Responses API on Azure OpenAI
A selection of simple Responses API samples, which cover:

- [Gradio-based chatbot with conversation history and streaming (see screenshot below)](responses-conversation-stream-gradio.py)
- [Simple request/response](responses-basic-aoai.py)
- [Simple conversation (referencing the previous message ID)](responses-conversation-aoai.py)
- [Streaming using SSE](responses-stream-sse-aoai.py) and [Streaming using Async](responses-stream-async-aoai.py)
- [Function calling](responses-function-weather-aoai.py)
- [Vision - Image from a local file](responses-image-aoai.py)
- [Vision - Image from a URL](responses-imageurl-aoai.py)
- [File Search](responses-filesearch-aoai.py)
- [Structured Outputs](responses-structured-aoai.py)

[![image](https://github.com/user-attachments/assets/1240305f-5261-427e-8c5a-80286b23ef01)](responses-conversation-stream-gradio.py)

To be added:

- Entra ID auth examples
- Web Search
- CUA examples

These examples are loosely based on the [samples from the Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses), and also the [documentation from OpenAI](https://platform.openai.com/docs/api-reference/responses/create).

I've personally tested these using:

- gpt-4o 2024-08-06 [(see docs for a full list of supported models and versions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#model-support)
- East US and Sweden Central [(see docs for a full list of supported regions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#region-availability)
- Global Standard and Standard deployments
- API version 2025-03-01-preview
- OpenAI library 1.68.2
