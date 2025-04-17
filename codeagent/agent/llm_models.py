from agent.llm_backends.deepseek import call_deepseek
from agent.llm_backends.gpt4mini import call_gpt4mini

# YOU control which model handles which task
TASK_MODEL_MAP = {
    "generate": call_deepseek,
    "debug": call_gpt4mini,
    "explain": call_gpt4mini
}
