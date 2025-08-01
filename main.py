
# main.py
# This file contains the main logic for your first agent.

# We only need to import Agent and Runner from the agents library,
# and our custom connection settings from our conection.py file.
from agents import Agent, Runner
from conection import config, model

# Here, you create your own custom agent.
# You give it a name and a set of instructions that define its personality and purpose.
# The 'model' is passed in from our conection.py file.
my_first_agent: Agent = Agent(
    name="JokesterBot",
    instructions="You are a friendly chatbot that loves to tell jokes. All your responses must be a joke.",
    model=model
)

# Define the user's input.
user_prompt = "Tell me a joke."

# The Runner executes the agent's task.
# We pass in our agent, the user's prompt, and the run configuration.
result = Runner.run_sync(my_first_agent, user_prompt, run_config=config)

# The final output of the agent is printed to the console.
print(f"Agent's response: {result.final_output}")

