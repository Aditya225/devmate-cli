from devmate.agents.debugger import debugger_agent
from devmate.agents.coder import coder_agent
from devmate.agents.planner import planner_agent
from crewai import Task,Crew
from devmate.tools.file_writter import write_file

def detect_language(user_input:str):
    text = user_input.lower()

    if "python" in text or ".py" in text:
        return "python" , "py"
    elif "node" in text or "javascript" in text or ".js" in text:
        return "node", "js"
    elif "typescript" in text or "ts" in text:
        return "typescript", "ts"
    elif "go" in text or "golang" in text:
        return "go", "go"
    elif "java" in text or "js" in text:
        return "java", "js"


def run_agent(task_input):
    planner = planner_agent
    coder = coder_agent
    debugger = debugger_agent

    task1 = Task(
        description=f"Break this into steps:{task_input}",
        expected_output="Step-by-step plan",
        agent = planner
    )

    lang,ext = detect_language(task_input)

    task2 =Task(
        description=f"""
        Create {lang} for: {task_input}

        Return strictly in this format:

        FILE: filename.{ext}
        CODE:
        <code only, no explanation>
        """,
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
    output = result.raw
    print("DEBUG RESULT:\n", result)
    # output = output.replace("```javacript","").replace("```", "").strip()
    output = output.replace("```", "").strip()
    from devmate.tools.file_writter import write_file
    if "FILE:" in output and "CODE:" in output:
        try:
            # remove comment markers
            output = output.replace("//", "")

            parts = output.split("CODE:")
            filename = parts[0].replace("FILE:", "").strip()
            code = parts[1].strip()

            
            write_file(f"output/{filename}", code)

            return f"✅ File created: output/{filename}"

        except Exception as e:
            return f"❌ Parsing error: {e}"

    filename = f"main.{ext}"
    write_file(f"output/{filename}", output)    
    
    # return "⚠️ Could not parse AI output"
    # if "const express" in output:
    #     from devmate.tools.file_writter import write_file
    #     write_file("output/server.js", output)

    #     return "✅ File created: output/server.js"

    # return output
    return f"⚠️ Default file created: output/{filename}"