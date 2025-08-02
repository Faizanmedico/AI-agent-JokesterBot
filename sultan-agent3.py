
from agents import Agent, Runner
from conection import get_config
agent: Agent = Agent(
    name="SultanAssistant",
    instructions="You are a brilliant historian specialized in Pakistan's history. Answer all questions truthfully and clearly."
)
question = "Who was the first Prime Minister of Pakistan?"
result = Runner.run_sync(agent, question, run_config=get_config())
print("Answer:", result.final_output)