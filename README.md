# Responses API on Azure OpenAI samples
Originally launched by OpenAI and now natively supported in Azure AI Foundry, the Responses API combines the simplicity of the Chat Completions API with the advanced tool-calling capabilities of the legacy Assistants API. It offers a streamlined way to build powerful agentic experiences by allowing developers to structure prompts, invoke tools, and manage outputs - all within a single API call.

This repo includes a selection of minimal Python samples covering the most of the common features of Responses API on Azure OpenAI:

| Sample description                                                                 | [Last generation API](#why-are-there-two-sets-of-samples-which-api-version-should-i-use) | [v1 API (GA)](#why-are-there-two-sets-of-samples-which-api-version-should-i-use)                  |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Simple request/response with API key auth                                                        | [responses-basic-aoai.py](python/responses-basic-aoai.py)                                                                                              | [responses-basic-aoai-v1.py](python/responses-basic-aoai-v1.py)                                                                                   |
| Simple request/response with Entra ID auth                                                        | [responses-basic-entra-aoai.py](python/responses-basic-entra-aoai.py)                                                                                              | [responses-basic-entra-aoai-v1.py](python/responses-basic-entra-aoai-v1.py)                                                                                |
 | Simple request/response with Entra ID auth                                                        | [responses-basic-entra-aoai.py](python/responses-basic-entra-aoai.py)                                                                                              | [responses-basic-entra-aoai-v1.py](python/responses-basic-entra-aoai-v1.py)                                                                                   |
| Stateless request/response with API key auth                                                      | n/a                                                                                                                                             | [responses-basic-stateless-aoai-v1.py](python/responses-basic-stateless-aoai-v1.py)                                                                           |
 | Simple conversation (referencing the previous message ID)                       | [responses-conversation-aoai.py](python/responses-conversation-aoai.py)                                                                                | [responses-conversation-aoai-v1.py](python/responses-conversation-aoai-v1.py)                                                                     |
| Simple conversation (referencing the previous message ID)                       | [responses-conversation-aoai.py](python/responses-conversation-aoai.py)                                                                                | [responses-conversation-aoai-v1.py](python/responses-conversation-aoai-v1.py)                                                                     |
| Streaming using SSE and Streaming using Async                                   | [responses-stream-sse-aoai.py](python/responses-stream-sse-aoai.py), [responses-stream-async-aoai.py](python/responses-stream-async-aoai.py)                  | [responses-stream-sse-aoai-v1.py](python/responses-stream-sse-aoai-v1.py), [responses-stream-async-aoai-v1.py](python/responses-stream-async-aoai-v1.py) |
| Function calling                                                                | [responses-function-weather-aoai.py](python/responses-function-weather-aoai.py)                                                                        | [responses-function-weather-aoai-v1.py](python/responses-function-weather-aoai-v1.py)                                                             |
| File Search                                                                     | [responses-filesearch-aoai.py](python/responses-filesearch-aoai.py)                                                                                    | [responses-filesearch-aoai-v1.py](python/responses-filesearch-aoai-v1.py)                                                                         |
| 🆕 PDF upload, via base64 (API key/Entra)                                            | n/a                                    | [responses-pdfupload-base64-aoai-v1.py](python/responses-pdfupload-base64-aoai-v1.py), [responses-pdfupload-base64-entra-aoai-v1.py](python/responses-pdfupload-base64-entra-aoai-v1.py)                                                                         |
| 🆕 PDF upload, via file upload (API key/Entra)                                       | n/a                                      | [responses-pdfupload-aoai-v1.py](python/responses-pdfupload-aoai-v1.py), [responses-pdfupload-aoai-entra-v1.py](python/responses-pdfupload-aoai-entra-v1.py)                                                                         |
| 🆕 Code Interpreter (API key/Entra)                                       | n/a                                      | [responses-codeinterpreter-aoai-v1.py](python/responses-codeinterpreter-aoai-v1.py), [responses-codeinterpreter-entra-aoai-v1.py](python/responses-codeinterpreter-entra-aoai-v1.py)                                                                         |
| Structured Outputs                                                              | [responses-structured-aoai.py](python/responses-structured-aoai.py)                                                                                    | [responses-structured-aoai-v1.py](python/responses-structured-aoai-v1.py)                                                                         |
| Reasoning                                                                       | [responses-reasoning-aoai.py](python/responses-reasoning-aoai.py)                                                                                      | [responses-reasoning-aoai-v1.py](python/responses-reasoning-aoai-v1.py)                                                                           |
| Vision: Image from a local file and Image from a URL                            | [responses-image-aoai.py](python/responses-image-aoai.py), [responses-imageurl-aoai.py](python/responses-imageurl-aoai.py)                                    | [responses-image-aoai-v1.py](python/responses-image-aoai-v1.py), [responses-imageurl-aoai-v1.py](python/responses-imageurl-aoai-v1.py)                   |
| Image generation using gpt-image-1 with API key auth                         | n/a                                                                                                                                             | [responses-image-generate-aoai-v1.py](python/responses-image-generate-aoai-v1.py)                                                                 |
| Image generation using gpt-image-1 with Entra ID auth                        | n/a                                                                                                                                             | [responses-image-generate-entra-aoai-v1.py](python/responses-image-generate-entra-aoai-v1.py)                                                     |
| Background mode                                                              | n/a                                                                                                                                             | [responses-background-aoai-v1.py](python/responses-background-aoai-v1.py)                                                                         |
| MCP remote server with API key auth                                                               | n/a                                                                                                                                             | [responses-mcp-aoai-v1.py](python/responses-mcp-aoai-v1.py)                                                                         |
| MCP remote server with Entra ID auth                                                            | n/a                                                                                                                                             | [responses-mcp-entra-aoai-v1.py](python/responses-mcp-entra-aoai-v1.py)                                                                         |
| MCP remote server with Gradio UI                                                            | n/a                                                                                                                                             | [responses-mcp-mslearn-gradio-aoai-v1.py](python/responses-mcp-mslearn-gradio-aoai-v1.py)                                                                         |
| Gradio-based chatbot with conversation history, image upload, Reasoning Summary | [responses-conversation-stream-gradio.py](python/responses-conversation-stream-gradio.py)                                                              | [responses-conversation-stream-gradio-v1.py](python/responses-conversation-stream-gradio-v1.py)                                                   |

[//]: # (Codespaces section inserted below)
## Quick Start with GitHub Codespaces

The quickest way to get started is using GitHub Codespaces, a hosted environment that is automatically set up for you. Click this button to create a Codespace (4-core machine recommended):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=Azure-Samples/azure-openai-responses-api-samples)

Wait for the Codespace to initialize. Python 3.12, Python extension, and dependencies will be automatically installed. For an even more streamlined experience, add the environment variables into your [Codespace user secrets](https://github.com/settings/codespaces).

## Why are there two sets of samples? Which API version should I use?
Starting in May 2025, you use the next generation v1 APIs which adds support for:
- Ongoing access to the latest features with no need to update api-version each month.
- OpenAI client support with minimal code changes to swap between OpenAI and Azure OpenAI when using key-based authentication.

Code samples have been provided for both the v1 API (now GA for Responses API), and also the older API versions. The v1 API samples have a v1.py suffix to distinguish them.

If you want the latest features, I would recommend using the v1 API. With the GA release, you no longer need to specify an api-version parameter.
If you need to use the older API versions, you can use the legacy samples. At time of writing, the latest GA API release is `2024-10-21`.

[Azure OpenAI in Azure AI Foundry Models API lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-lifecycle?tabs=key#api-evolution)

## Microsoft Agent Framework and Semantic Kernel
[Microsoft Agent Framework](https://aka.ms/agentframework) has supported Responses API for both Azure OpenAI and OpenAI since the initial public preview on 1st October 2025 (version 1.0.0b251001). The following Azure OpenAI samples provide code for image analysis, function calling, conversation threads, and code interpreter.

[Azure OpenAI Agent Examples](https://github.com/microsoft/agent-framework/tree/main/python/samples/getting_started/agents/azure_openai)

As of 1.27, Semantic Kernel supports Responses API for both Azure OpenAI and OpenAI. The following samples provide examples for conversation history, plugins, Web Search (currently OpenAI only), File Search, vision, and Structured Outputs.

[Getting started with Responses API in Semantic Kernel](https://github.com/microsoft/semantic-kernel/tree/main/python/samples/getting_started_with_agents/openai_responses)


## Recommended settings

If you're coming to this for the first time, and want some suggestions for the most compatible/simplest way to try out the latest features, try the following:

- Model: gpt-4.1 [(see docs for a full list of supported models and versions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#model-support)
- Region: East US2 or Sweden Central [(see docs for a full list of supported regions)](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses?tabs=python-secure#region-availability)
- Deployment: Global Standard
- API version: v1 (GA)
- If using the "Legacy" API version: 2025-04-01-preview
- OpenAI library 1.99.2 or above (ideally the latest stable release)
- Semantic Kernel 1.36.1 or above (ideally the latest stable release)

[![Reasoning Summary](https://github.com/user-attachments/assets/9e1ab1b8-8c3d-4ccf-911e-3c7711abe947)](python/responses-conversation-stream-gradio.py)

## Features currently unsupported on Responses API on Azure OpenAI
- web_search tool (Azure AI Foundry Agent Service recommended if web search is needed)

## Further reading
- [The Responses API in Azure AI Foundry is now generally available](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/the-responses-api-in-azure-ai-foundry-is-now-generally-available/4446567)
- [Introducing New Tools and Features in the Responses API in Azure AI Foundry](https://devblogs.microsoft.com/foundry/introducing-new-tools-and-features-in-the-responses-api-in-azure-ai-foundry/)
- [Announcing the Responses API and Computer-Using Agent in Azure AI Foundry](https://azure.microsoft.com/blog/announcing-the-responses-api-and-computer-using-agent-in-azure-ai-foundry/)
- [Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses)
- [Azure OpenAI in Azure AI Foundry Models v1 REST API reference](https://learn.microsoft.com/azure/ai-foundry/openai/latest#create-response)
- [OpenAI documentation](https://platform.openai.com/docs/api-reference/responses/create)

## Attribution and thanks
These examples are loosely based on [@mrbullwinkle's](https://github.com/mrbullwinkle) samples from the [Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses), and also helped by the [documentation from OpenAI](https://platform.openai.com/docs/api-reference/responses/create). Thanks to [@moonbox3](https://github.com/moonbox3) for providing the Semantic Kernel and Microsoft Agent Framework samples. Thanks to Rafal Rutyna for providing useful information on the May 2025 updates.
