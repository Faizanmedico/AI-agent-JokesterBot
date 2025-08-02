from agents import Agent, Runner
from conection import config, model
agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)
print(result.final_output)










agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")
result = Runner.run_sync(agent, "Hello", run_config=config )
print(result.final_output)
