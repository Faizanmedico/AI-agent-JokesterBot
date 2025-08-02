# main_personal_agent.py
# This file defines and runs an interactive agent that uses the user's name in its responses.

from agents import Agent, Runner
from conection import config, model

# Define our new agent with a key instruction: to always use the user's name.
personal_agent: Agent = Agent(
    name="PersonalAssistant",
    instructions="You are a friendly and helpful assistant. The user's name is 'Sultan'. Always address the user as Sultan in your responses. Your goal is to provide concise and polite answers.",
    model=model
)

# Start the interactive session.
print("--- Welcome to your Personal Assistant ---")
print("I'm ready to help you, Sultan!")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for their question.
        user_question = input("Sultan, what can I help you with today? ")
        
        # Exit the loop if the user types 'quit' or 'exit'.
        if user_question.lower() in ["quit", "exit"]:
            print("Goodbye, Sultan! Have a great day!")
            break

        if not user_question.strip():
            continue
        
        # The prompt sent to the agent is now the user's question directly.
        # The instructions handle the personalization.
        print("\nProcessing...")
        result = Runner.run_sync(personal_agent, user_question, run_config=config)
        agent_response = result.final_output

        # Print the agent's response.
        print(f"\nAssistant's reply: {agent_response}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

