import sys
from devmate.core.executor  import run_agent

def main():
    if len(sys.argv) < 2:
        print("Usage: devmate 'your task'")
        return

    task = " ".join(sys.argv[1:])   # 🔥 fix
    run_agent(task)


if __name__ == "__main__":
    main()