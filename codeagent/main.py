from agent.tasks import run_task

def main():
    print("🧠 CodeAgent CLI v1")
    print("Available Tasks: generate, debug, explain\n")

    while True:
        task = input("Task type (or 'exit'): ").strip().lower()
        if task == "exit":
            break

        model = input("Model (deepseek_r1 / gpt4_mini / ...): ").strip()
        user_input = input("Enter your code or request:\n")

        try:
            result = run_task(task, user_input, model_name=model)
            print("\n🤖 Agent Response:\n")
            print(result)
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
