# conection.py
# This file sets up the connection to the Gemini API by reading the API key from a .env file.

# Import the load_dotenv function to read key-value pairs from .env
from dotenv import load_dotenv
import os

from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables from the .env file.
# This must be called before trying to access any variables.
load_dotenv()

# Get the API key from the environment.
# The `os.getenv()` function retrieves the value of the environment variable.
# It's a good practice to handle the case where the key might be missing.
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key was successfully loaded.
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")

# Initialize the AsyncOpenAI client.
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model to be used.
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash-preview-05-20",
    openai_client=external_client
)

# Create the RunConfig object.
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
