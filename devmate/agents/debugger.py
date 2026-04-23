from crewai import Agent
from devmate.config.llm import get_llm

debugger_agent = Agent(
    role="Debugger",
    goal="Fix bugs in code",
    backstory="Expert software debugger",
    llm=get_llm(),
    verbose=True
)