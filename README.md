# Responses API samples
A selection of simple Responses API samples, which cover:

| Sample description                                                                 | [Previous generation API (202x-xx-xx)](#why-are-there-two-sets-of-samples-which-api-version-should-i-use) | [v1 preview API](#why-are-there-two-sets-of-samples-which-api-version-should-i-use)                  |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Gradio-based chatbot with conversation history, image upload, Reasoning Summary | [responses-conversation-stream-gradio.py](src/responses-conversation-stream-gradio.py)                                                              | [responses-conversation-stream-gradio-v1.py](src/responses-conversation-stream-gradio-v1.py)                                                   |
| Simple request/response with API key auth                                                        | [responses-basic-aoai.py](src/responses-basic-aoai.py)                                                                                              | [responses-basic-aoai-v1.py](src/responses-basic-aoai-v1.py)                                                                                   |
| Simple request/response with Entra ID auth                                                        | [responses-basic-entra-aoai.py](src/responses-basic-entra-aoai.py)                                                                                              | [responses-basic-entra-aoai-v1.py](src/responses-basic-entra-aoai-v1.py)                                                                                   |
| Simple conversation (referencing the previous message ID)                       | [responses-conversation-aoai.py](src/responses-conversation-aoai.py)                                                                                | [responses-conversation-aoai-v1.py](src/responses-conversation-aoai-v1.py)                                                                     |
| Streaming using SSE and Streaming using Async                                   | [responses-stream-sse-aoai.py](src/responses-stream-sse-aoai.py), [responses-stream-async-aoai.py](src/responses-stream-async-aoai.py)                  | [responses-stream-sse-aoai-v1.py](src/responses-stream-sse-aoai-v1.py), [responses-stream-async-aoai-v1.py](src/responses-stream-async-aoai-v1.py) |
| Function calling                                                                | [responses-function-weather-aoai.py](src/responses-function-weather-aoai.py)                                                                        | [responses-function-weather-aoai-v1.py](src/responses-function-weather-aoai-v1.py)                                                             |
| File Search                                                                     | [responses-filesearch-aoai.py](src/responses-filesearch-aoai.py)                                                                                    | [responses-filesearch-aoai-v1.py](src/responses-filesearch-aoai-v1.py)                                                                         |
| Structured Outputs                                                              | [responses-structured-aoai.py](src/responses-structured-aoai.py)                                                                                    | [responses-structured-aoai-v1.py](src/responses-structured-aoai-v1.py)                                                                         |
| Reasoning                                                                       | [responses-reasoning-aoai.py](src/responses-reasoning-aoai.py)                                                                                      | [responses-reasoning-aoai-v1.py](src/responses-reasoning-aoai-v1.py)                                                                           |
| Vision: Image from a local file and Image from a URL                            | [responses-image-aoai.py](src/responses-image-aoai.py), [responses-imageurl-aoai.py](src/responses-imageurl-aoai.py)                                    | [responses-image-aoai-v1.py](src/responses-image-aoai-v1.py), [responses-imageurl-aoai-v1.py](src/responses-imageurl-aoai-v1.py)                   |
| 🆕 Image generation using gpt-image-1 with API key auth                         | n/a                                                                                                                                             | [responses-image-generate-aoai-v1.py](src/responses-image-generate-aoai-v1.py)                                                                 |
| 🆕 Image generation using gpt-image-1 with Entra ID auth                        | n/a                                                                                                                                             | [responses-image-generate-entra-aoai-v1.py](src/responses-image-generate-entra-aoai-v1.py)                                                     |
| 🆕 Background mode                                                              | n/a                                                                                                                                             | [responses-background-aoai-v1.py](src/responses-background-aoai-v1.py)                                                                         |
| 🆕 MCP remote server with API key auth                                                               | n/a                                                                                                                                             | [responses-mcp-aoai-v1.py](src/responses-mcp-aoai-v1.py)                                                                         |
| 🆕 MCP remote server with Entra ID auth                                                            | n/a                                                                                                                                             | [responses-mcp-entra-aoai-v1.py](src/responses-mcp-entra-aoai-v1.py)                                                                         |

[![Reasoning Summary](https://github.com/user-attachments/assets/9e1ab1b8-8c3d-4ccf-911e-3c7711abe947)](src/responses-conversation-stream-gradio.py)

# Why are there two sets of samples? Which API version should I use?
Starting in May 2025, you can now opt in to our next generation of v1 Azure OpenAI APIs which add support for:
- Ongoing access to the latest features with no need to update api-version each month.
- OpenAI client support with minimal code changes to swap between OpenAI and Azure OpenAI when using key-based authentication.

Code samples have been provided for both the v1 API Preview, and also the older API versions. The v1 API Preview samples have a v1.py suffix to distinguish them.

If you want the latest features, I would recommend using the v1 API Preview, with the `api-version` set to `preview`.
If you need a stable, GA version, and don't need the latest features, then you can use the older API. At time of writing, the latest GA API release is `2024-10-21`.

[Azure OpenAI in Azure AI Foundry Models API lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-lifecycle?tabs=key#api-evolution)

# Semantic Kernel 
As of 1.27, Semantic Kernel supports Responses API for both Azure OpenAI and OpenAI. The following samples provide examples for conversation history, plugins, Web Search (currently OpenAI only), File Search, vision, and Structured Outputs.

[Getting started with Responses API in Semantic Kernel](https://github.com/microsoft/semantic-kernel/tree/main/python/samples/getting_started_with_agents/openai_responses)

# Recommended settings

I've personally tested these Responses API samples using:

- gpt-4o 2024-08-06, gpt-4.1, o4-mini, and more [(see docs for a full list of supported models and versions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#model-support)
- East US and Sweden Central [(see docs for a full list of supported regions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#region-availability)
- Global Standard and Standard deployments
- API version 2025-03-01-preview (2025-04-01-preview if using Reasoning Summaries)
- OpenAI library 1.68.2 or above
- Semantic Kernel 1.27 or above

# Features currently unsupported on Responses API on Azure OpenAI
- web_search tool (Azure AI Foundry Agent Service recommended if web search is needed)
- Code Interpreter (again, Azure AI Foundry Agent Service supports this if required)

# Further reading
- [Introducing New Tools and Features in the Responses API in Azure AI Foundry](https://devblogs.microsoft.com/foundry/introducing-new-tools-and-features-in-the-responses-api-in-azure-ai-foundry/)
- [Announcing the Responses API and Computer-Using Agent in Azure AI Foundry](https://azure.microsoft.com/blog/announcing-the-responses-api-and-computer-using-agent-in-azure-ai-foundry/)
- [Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses)
- [OpenAI documentation](https://platform.openai.com/docs/api-reference/responses/create)

# Attribution
These examples are loosely based on [@mrbullwinkle's](https://github.com/mrbullwinkle) samples from the [Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses), and also helped by the [documentation from OpenAI](https://platform.openai.com/docs/api-reference/responses/create). Thanks to [@moonbox3](https://github.com/moonbox3) for providing the Semantic Kernel samples. Thanks to Rafal Rutyna for providing useful information on the May 2025 updates.
