from devmate.agents.debugger import debugger_agent
from devmate.agents.coder import coder_agent
from devmate.agents.planner import planner_agent
from crewai import Task,Crew
 

def run_agent(task_input):
    planner = planner_agent
    coder = coder_agent
    debugger = debugger_agent

    task1 = Task(
        description=f"Break this into steps:{task_input}",
        expected_output="Step-by-step plan",
        agent = planner
    )

    task2 =Task(
        description=f"Code: {task_input}",
        expected_output="Working code",
        agent= coder
    )

    task3 = Task(
        description=f"Debug: {task_input}",
        expected_output="Bug-free code",
        agent= debugger
    )
    

    crew = Crew(
        agents=[planner,coder,debugger],
        tasks=[task1,task2,task3],
        verbose= True
    )

    result = crew.kickoff()
    return result
   