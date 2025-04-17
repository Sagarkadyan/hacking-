from agent.tasks import run_task
from agent.history import init_db, log_interaction, get_history
from agent.runner import run_code
from agent.memory import init_memory, add_memory, search_memory

import os

def main():
    print("🧠 CodeAgent CLI v2")
    print("Tasks: generate, debug, explain")
    print("Commands: history, memory, run, exit")

    os.makedirs("storage", exist_ok=True)
    init_db()
    init_memory()

    while True:
        command = input("\nCommand or task type: ").strip().lower()
        if command == "exit":
            break
        elif command == "history":
            history = get_history()
            for row in history:
                print(f"🕓 {row[4]} | {row[0]} | {row[1]}")
                print(f"🧑‍💻 {row[2]}")
                print(f"🤖 {row[3][:200]}...\n")
        elif command == "memory":
            action = input("Add or search? ").strip().lower()
            if action == "add":
                label = input("Label: ")
                content = input("Content: ")
                add_memory(label, content)
                print("✅ Memory added.")
            elif action == "search":
                keyword = input("Keyword: ")
                results = search_memory(keyword)
                for r in results:
                    print(f"📌 {r[0]}: {r[1]}")
        elif command == "run":
            code = input("Paste Python code to run:\n")
            result = run_code(code)
            print(f"📤 Output:\n{result}")
        elif command in ["generate", "debug", "explain"]:
            model = input("Model (deepseek_r1 / gpt4_mini): ").strip()
            user_input = input("Enter your code or request:\n")
            try:
                result = run_task(command, user_input, model_name=model)
                print("\n🤖 Agent Response:\n")
                print(result)
                log_interaction(command, model, user_input, result)

                save = input("Save output to file? (y/n): ").strip().lower()
                if save == "y":
                    filename = input("Filename (e.g. mycode.py): ").strip()
                    with open(filename, "w") as f:
                        f.write(result)
                    print(f"✅ Saved to {filename}")
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
