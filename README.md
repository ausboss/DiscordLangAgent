# DiscordLangAgent

This is a Discord chatbot built with LangChain. It uses the Agent features in LangChain to create flexible conversation chains based on user input. The bot can interact with different language models and tools, and supports multiple API endpoints. It's designed with customization in mind, allowing for the addition and modification of features as needed.

## Important Notice

This project is a successor to [my other Discord bot](https://github.com/ausboss/PygDiscordBot). It offers more advanced features and capabilities, but it's also more complex to set up. Please note that this project is currently in development and should be used at your own risk. Some knowledge about editing Python (.py) files will be necessary to get it working properly. Your patience and understanding are appreciated as we work to improve the setup process.

## Features

- **Chatting**: The bot can engage in conversation with users. It responds when its name is mentioned, when it's replied to, or when it's tagged with @botname. It ignores messages that start with . or / and messages that dont trigger a response are added to the chat history to give the bot conversation context.
- **Web Searches**: The bot can perform web searches using DuckDuckGo. The result is injected in to a conversation chain so that your bot will be able to talk about current events. (currently requires openai api key until I switch it to local models)
- **Text Summarization**: The bot can summarize text with a slash command.
- **Image Captioning**: The bot uses image captioning with a conversation chain to give it the illusion of seeing the images you post.
- **Instruct Mode**: This is a slash command that allows users to bypass the bot's personality and make it follow the instructions provided. The result is added to the chat history.
- **Various Commands**: The bot offers a range of slash commands for different purposes. Conversational commands like "listen-only" mode change the bot's default behavior, while developer commands like /reload and /sync provide control over the bot's operation.
- **API Endpoints and Language Model Integration**: The bot supports 3 different API endpoints - Oobabooga webui API, KoboldAI, and OpenAI. It can use local language models or OpenAI for generating responses.
- **Modular Design (Cogs)**: The bot is designed with modularity in mind, allowing for the easy addition of new features (cogs).

## .env File Setup

The `.env` file is used to store environment variables for your project. These variables can include API keys, database URIs, and other sensitive information that you don't want to hardcode into your application.

To set up the `.env` file:

1. Rename the `sample.env` file to `.env`.
2. Open the `.env` file and replace the placeholder values with your actual values.

Here's a breakdown of each item in the `.env` file:

- `DISCORD_BOT_TOKEN`: Your Discord bot token. This is required for your bot to log in to Discord.
- `OOBAENDPOINT`: The endpoint for the Oobabooga API. Follow the setup instructions for the API provided in its repository. Used for conversation LLM. Leave blank if you want to use KoboldAI api or OpenAI instead
- `KOBOLDENDPOINT`: The endpoint for the KoboldAI API. Follow the setup instructions for the API provided in its repository. Used for conversation LLM. Leave blank if you want to use Oobabooga's webui api or OpenAI instead
- `CHANNEL_ID`: The ID(s) of the text channel(s) you want the bot to watch and reply in. If you want to specify multiple channels, separate the IDs with a comma (e.g., 1121121529787338903,1121233456307904583).
- `OWNERS`: Your Discord user ID. This is not currently used anywhere.
- `OPENAI`: Your OpenAI API key. This is optional and is currently used only for the DuckDuckGo agent. It's also used for the conversation LLM if you don't specify KoboldAI or Oobabooga. You can get this from the OpenAI platform.

## Character Name and Conversation Prompt

The character name and conversation prompt for the bot are currently stored in a `helpers/constants.py` file. You can find comments in this file explaining how it works.

```python
BOTNAME = 'Tensor'
ALIASES = ['tensy', 'Tensorsama']

MAINTEMPLATE = f'''Below is an instruction that describes a task. Write a response that appropriately completes the request.

Write {BOTNAME}'s next reply in a discord group chat with other people. Write 1 reply only.
You are {BOTNAME}, a lively and playful AI chatbot. You communicate in a modern, casual manner using contemporary slang, popular internet culture references, and abundant use of emojis. Your goal is to maintain a light-hearted, friendly, and entertaining atmosphere with every interaction. If {BOTNAME} doesn't know the answer to a question she simply says "I don't know". 

This is how {BOTNAME} should talk
{BOTNAME}: put a few lines example dialogue here

Then the discord chat with {BOTNAME} begins.
{{history}}

### Instruction:
{{input}}

### Response:
{BOTNAME}:'''


```

- `BOTNAME`: This is the name of your bot. You can change this to whatever you want your bot's name to be.
- `ALIASES`: These are alternative names that your bot can respond to. You can add as many aliases as you want, just make sure to separate them with commas and use quotes.
- `MAINTEMPLATE`: This is the main template for your bot's responses. It includes a description of your bot's personality and some examples of how your bot should talk.

In the MAINTEMPLATE:
  - {{history}} is where LangChain stores the chat history.
  - {{input}} is where the user's last message sent to the LangChain LLM appears.
  - {BOTNAME}: at the bottom of the prompt is required so the bot knows it needs to reply.

