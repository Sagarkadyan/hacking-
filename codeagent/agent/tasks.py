from agent.llm_models import TASK_MODEL_MAP

def run_task(task_type, user_input, model_name=None):
    if task_type not in TASK_MODEL_MAP:
        raise ValueError("Unsupported task type")
    return TASK_MODEL_MAP[task_type](user_input)
