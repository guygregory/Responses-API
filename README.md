# Responses API samples
A selection of simple Responses API samples, which cover:

- [Gradio-based chatbot with conversation history, image upload, streaming, and 🆕 Reasoning Summary (see screenshot below)](responses-conversation-stream-gradio.py)
- [Simple request/response](responses-basic-aoai.py)
- [Simple conversation (referencing the previous message ID)](responses-conversation-aoai.py)
- [Streaming using SSE](responses-stream-sse-aoai.py) and [Streaming using Async](responses-stream-async-aoai.py)
- [Function calling](responses-function-weather-aoai.py)
- [File Search](responses-filesearch-aoai.py)
- [Structured Outputs](responses-structured-aoai.py)
- [Reasoning](responses-reasoning-aoai.py)
- Vision: [Image from a local file](responses-image-aoai.py) and [Image from a URL](responses-imageurl-aoai.py)

[![Reasoning Summary](https://github.com/user-attachments/assets/9e1ab1b8-8c3d-4ccf-911e-3c7711abe947)](responses-conversation-stream-gradio.py)

# Semantic Kernel 
As of 1.27, Semantic Kernel supports Responses API for both Azure OpenAI and OpenAI. The following samples provide examples for conversation history, plugins, Web Search (currently OpenAI only), File Search, vision, and Structured Outputs.

[Getting started with Responses API in Semantic Kernel](https://github.com/microsoft/semantic-kernel/tree/main/python/samples/getting_started_with_agents/openai_responses)

# Recommended settings

I've personally tested these Responses API samples using:

- gpt-4o 2024-08-06 [(see docs for a full list of supported models and versions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#model-support)
- East US and Sweden Central [(see docs for a full list of supported regions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#region-availability)
- Global Standard and Standard deployments
- API version 2025-03-01-preview (2025-04-01-preview if using Reasoning Summaries)
- OpenAI library 1.68.2 or above
- Semantic Kernel 1.27 or above

# Attribution
These examples are loosely based on [@mrbullwinkle's](https://github.com/mrbullwinkle) samples from the [Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses), and also helped by the [documentation from OpenAI](https://platform.openai.com/docs/api-reference/responses/create). Thanks to [@moonbox3](https://github.com/moonbox3) for providing the Semantic Kernel samples.
