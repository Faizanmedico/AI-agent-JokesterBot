from conection import get_config
from agents import Agent, Runner
# No need for specific chat_prompt import if we define instructions directly

# Get the run configuration
run_config = get_config()

# Define a simple Agent
# This Agent will use the model from run_config for its "instructions"
# The instructions guide the model's behavior.
greeter_agent = Agent(
    name="Greeter",
    instructions="You are a polite assistant. Your only task is to greet people.",
    model=run_config.model, # Assign the configured model to the agent
    # No tools needed for a simple greeting
    tools=[]
)

# Define the input for the agent
agent_input = "Say hello to Sultan."

# Run the agent with the input using the Runner
# The Runner will now correctly interact with the Agent
# and use the agent's assigned model.
result = Runner.run_sync(greeter_agent, agent_input)

# The final_output typically contains the model's response
print(result.final_output)