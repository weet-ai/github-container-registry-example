from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv

load_dotenv()

def get_model(model = "gpt-4.1"):
    """
        Get the chat model for the specified version.
        OPENAI_API_URL and OPENAI_API_KEY must have been
        setup.
    """

    client = AsyncOpenAI(base_url = os.getenv("OPENAI_API_URL"))
    return OpenAIChatCompletionsModel(openai_client = client, model=model)
