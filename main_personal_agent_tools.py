# main_fact_checker.py
# This file defines and runs an agent that uses the google_search tool.

from agents import Agent, Runner
from conection import config, model
# We import the google_search tool directly.
from google_search import search

# Define our new agent with instructions to use the search tool.
# This agent's persona is a helpful search assistant.
fact_checker_agent: Agent = Agent(
    name="FactChecker",
    instructions=(
        "You are a helpful assistant. Your goal is to provide accurate and up-to-date information. "
        "You have access to a tool named `search` which performs a Google Search. "
        "Use this tool to answer any questions that require current, real-time information. "
        "If the answer is a simple fact, provide it directly. "
        "If the user asks a question that requires a search, use the search tool to find the information before answering. "
        "If a question doesn't require a search, use your own knowledge."
    ),
    model=model
)

# Start the interactive session.
print("--- Welcome to the Fact-Checker Agent ---")
print("I can answer your questions by searching the web. Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for their question.
        user_question = input("Your question: ")
        
        if user_question.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break

        if not user_question.strip():
            continue
        
        print("\nSearching and processing...")
        
        # We now pass the pre-built 'search' function to the Runner as our tool.
        # This is a much more reliable way to use a tool.
        result = Runner.run_sync(
            fact_checker_agent,
            user_question,
            run_config=config,
            tools=[search]  # We pass the search function itself.
        )
        agent_response = result.final_output

        print(f"\nAnswer: {agent_response}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break
