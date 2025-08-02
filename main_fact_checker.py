# main_fact_checker.py
# This file defines and runs an agent that answers fact-based questions
# using a pre-loaded dictionary to simulate a search tool.

from agents import Agent, Runner
from conection import config, model

# A dictionary to simulate a tool's knowledge.
# This is a simple way to give the agent "external" information.
common_knowledge = {
    "capital of pakistan": "Islamabad is the capital of Pakistan.",
    "software testing": "Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do.",
    "pst vs pkt": "PST (Pacific Standard Time) is UTC-8, and PKT (Pakistan Standard Time) is UTC+5. This means PKT is 13 hours ahead of PST.",
    "who won the world cup in 2022": "Argentina won the World Cup in 2022."
}

# Define our agent. Its instructions are now key.
fact_checker_agent: Agent = Agent(
    name="FactChecker",
    instructions=(
        "You are a helpful and accurate fact-checker. "
        "The user will ask you questions. If a question is about the capital of Pakistan, "
        "software testing, the difference between PST and PKT, or who won the World Cup in 2022, "
        "you must use the information provided to you and not your own knowledge. "
        "For all other questions, use your general knowledge. "
        "Answer concisely and politely."
    ),
    model=model
)

# Start the interactive session.
print("--- Welcome to the Fact-Checker Agent ---")
print("I can answer a few specific questions for you. Type 'quit' or 'exit' to end the session.\n")
print("Try asking about 'the capital of Pakistan' or 'PST vs PKT'.")

while True:
    try:
        # Get user input for their question.
        user_question = input("\nYour question: ")
        
        if user_question.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break

        if not user_question.strip():
            continue
        
        # We find the answer from our pre-loaded knowledge, if it exists.
        found_answer = None
        for key, value in common_knowledge.items():
            if key in user_question.lower():
                found_answer = value
                break
        
        # We now run the agent. We provide the answer from our "tool" in the prompt itself.
        if found_answer:
            prompt = f"The user asked: '{user_question}'. Here is the information you must use: '{found_answer}'."
        else:
            prompt = f"The user asked: '{user_question}'. Answer based on your general knowledge."
            
        print("\nProcessing...")
        
        result = Runner.run_sync(
            fact_checker_agent,
            prompt,  # The prompt now includes the tool's result.
            run_config=config,
        )
        agent_response = result.final_output

        print(f"\nAnswer: {agent_response}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

