# main_translator.py
# This file defines and runs an interactive agent that translates English to Urdu.

# We reuse the same connection settings.
from agents import Agent, Runner
from conection import config, model

# Define our new agent with instructions to be a translator.
translator_agent: Agent = Agent(
    name="UrduTranslator",
    instructions="You are an expert translator. Your sole purpose is to translate text from English to Urdu. Provide only the translated text, without any additional explanations.",
    model=model
)

# Start the interactive translation experience.
print("--- Welcome to the English to Urdu Translator ---")
print("Enter an English phrase to get the translation.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for the text they want to translate.
        english_text = input("English text: ")
        
        # Exit the loop if the user types 'quit' or 'exit'.
        if english_text.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break

        # Check if the user entered an empty line.
        if not english_text.strip():
            continue

        # Run the agent with the English text.
        print("\nTranslating...")
        result = Runner.run_sync(translator_agent, english_text, run_config=config)

        # Print the agent's translated response.
        print(f"Urdu Translation: {result.final_output}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        # Break the loop to avoid continuous errors.
        break

