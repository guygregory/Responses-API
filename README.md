# Responses API on Azure OpenAI
A selection of basic Responses API on Azure OpenAI samples, which cover:

- [Simple request/response](responses-basic-aoai.py)
- [Conversation (referencing the previous message ID)](responses-conversation-aoai.py)
- [Function calling](responses-function-weather-aoai.py)
- [Vision](responses-image-aoai.py)

To be added:

- Structured Outputs
- Streaming responses
- Entra ID auth examples

These examples are loosely based on the [samples from the Microsoft Learn Documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/responses), and also the [documentation from OpenAI](https://platform.openai.com/docs/api-reference/responses/create).

I've personally tested these using:

- gpt-4o 2024-08-06
- East US
- Global Standard
- API version 2025-03-01-preview
- OpenAI library 1.68.2
