from .models import call_model

def run_task(task_type, user_input, model_name="deepseek_r1"):
    system_msg = {"role": "system", "content": "You are a helpful code assistant."}

    if task_type == "generate":
        user_msg = {"role": "user", "content": f"Write a Python function for:\n{user_input}"}
    elif task_type == "debug":
        user_msg = {"role": "user", "content": f"Fix bugs in this code:\n{user_input}"}
    elif task_type == "explain":
        user_msg = {"role": "user", "content": f"Explain this code in simple terms:\n{user_input}"}
    else:
        user_msg = {"role": "user", "content": user_input}

    return call_model(model_name, [system_msg, user_msg])
