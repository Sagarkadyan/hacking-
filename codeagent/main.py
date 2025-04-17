from agent.tasks import run_task

def main():
    while True:
        task = input("Task (generate/debug/explain/exit): ")
        if task == "exit":
            break
        user_input = input("Enter your input: ")
        output = run_task(task, user_input)
        print("OUTPUT:", output)

if __name__ == "__main__":
    main()
