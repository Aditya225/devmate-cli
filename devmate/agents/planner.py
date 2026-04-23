from crewai import Agent
from devmate.config.llm import get_llm

planner_agent = Agent(
    role="Planner",
    goal="Break down tasks",
    backstory="Expert software architect",
    llm=get_llm(),
    verbose=True
)