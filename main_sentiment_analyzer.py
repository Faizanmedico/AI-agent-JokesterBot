# main_sentiment_analyzer.py
# This file defines and runs an interactive agent that analyzes text sentiment.

# We reuse the same connection settings.
from agents import Agent, Runner
from conection import config, model

# Define our new agent with instructions to be a sentiment analyzer.
sentiment_agent: Agent = Agent(
    name="SentimentAnalyzer",
    instructions="You are an expert sentiment analyzer. Your task is to analyze a given text and classify its sentiment as either 'Positive', 'Negative', or 'Neutral'. Provide only the classification and nothing else.",
    model=model
)

# Use a loop to create an interactive sentiment analysis experience.
print("--- Welcome to the Sentiment Analyzer ---")
print("Enter a sentence or paragraph to analyze its sentiment.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for the text they want to analyze.
        text_to_analyze = input("Text to analyze: ")
        
        # Exit the loop if the user types 'quit' or 'exit'.
        if text_to_analyze.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break

        # Check for empty input.
        if not text_to_analyze.strip():
            continue

        # Run the agent with the text to analyze.
        print("\nAnalyzing...")
        result = Runner.run_sync(sentiment_agent, text_to_analyze, run_config=config)
        sentiment_result = result.final_output

        # Print the sentiment classification.
        print(f"Sentiment: {sentiment_result}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

