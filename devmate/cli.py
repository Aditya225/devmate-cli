import sys
from devmate.core.executor  import run_agent



def chat_mode():
    print("🚀 DevMate AI Assistant (type 'exit' to quit)\n")

    chat_history = []
    cache ={}
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit","quit"]:
            print("GoodBye")
            return
        if not user_input.strip():
            continue
        key = user_input.lower()
        if key in cache:
            print("\n⚡ (cached response)\n")
            print(cache[key])
            return cache
        
        chat_history.append(f"User:{user_input}")
        full_context = "\n".join(chat_history)

        try:
            print("\nAI is thinking...\n")
            result = run_agent(full_context)
            cache[key] = result
            chat_history.append(f"AI:{result}")
            print(f"\nAI:\n{result}\n")
        except Exception as e:
            print(f"Error: {e}")   


def main():
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])   # 🔥 fix
        run_agent(task)
    else:
        chat_mode()        

if __name__ == "__main__":
    main()