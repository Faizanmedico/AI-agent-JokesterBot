# main_storyteller.py
# This file defines and runs a new agent that tells stories.

# We reuse the same connection settings from the conection.py file.
from agents import Agent, Runner
from conection import config, model

# Define our new agent.
# This time, the agent's instructions are to be a creative writer.
my_storyteller_agent: Agent = Agent(
    name="Storyteller",
    instructions="You are a brilliant and imaginative storyteller. Your purpose is to write short, engaging stories based on a user's prompt.",
    model=model
)

# Define the user's prompt for a new story.
user_prompt = "Write a short story about a brave knight who finds a lost dragon egg."

# Run the new agent with our new prompt.
result = Runner.run_sync(my_storyteller_agent, user_prompt, run_config=config)

# Print the agent's response, which will be the story.
print(f"--- The Storyteller's Tale ---\n\n{result.final_output}")

