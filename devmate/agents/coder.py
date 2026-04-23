from crewai import Agent
from devmate.config.llm import get_llm


coder_agent = Agent(
    role="Coder",
    goal="Write clean code",
    backstory="Expert developer",
    llm=get_llm(),
    verbose=True
)  
