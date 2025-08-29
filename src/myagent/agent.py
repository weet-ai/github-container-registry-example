from agents import Agent, Runner, function_tool, set_tracing_disabled
from datetime import datetime
from src.myagent.model import get_model

set_tracing_disabled(True)

@function_tool
async def get_current_time():
    return datetime.now().isoformat()

agent = Agent(
    name = "SimpleAgent",
    instructions = "A simple agent that returns the current time.",
    tools = [get_current_time],
    model = get_model()
)

async def run(prompt: str):

    result = await Runner.run(starting_agent = agent, input = prompt)
    return result.final_output
