# CDP Agentkit Twitter Langchain Extension Examples - Chatbot

This example demonstrates an agent setup as a terminal style chatbot with access to the full set of CDP Agentkit Twitter Langchain actions.

## Ask the chatbot to engage in the Twitter (X) ecosystem!
- "Transfer a portion of your ETH to john2879.base.eth"
- "What are my twitter account details?"
- "Please post a hello, world! to twitter"
- "Please monitor my mentions"
- "Please stop monitoring my mentions"

## Requirements
- Python 3.10+
- [OpenAI API Key](https://platform.openai.com/docs/quickstart#create-and-export-an-api-key)
- [Twitter (X) Keys](https://developer.x.com/en/portal/projects-and-apps)

### Checking Python Version
Before using the example, ensure that you have the correct version of Python installed. The example requires Python 3.10 or higher. You can check your Python version by running the following code:

```bash
python --version
pip --version
```

## Installation
```bash
pip install twitter-langchain
```

## Run the Chatbot

### Set ENV Vars
- Ensure the following ENV Vars are set:
  - "OPENAI_API_KEY"
  - "TWITTER_ACCESS_TOKEN"
  - "TWITTER_ACCESS_TOKEN_SECRET"
  - "TWITTER_API_KEY"
  - "TWITTER_API_SECRET"
  - "TWITTER_BEARER_TOKEN"

```bash
python chatbot.py
```
