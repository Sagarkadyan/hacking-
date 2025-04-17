import requests
from .config import MODEL_APIS

def call_model(model_name, messages, temperature=0.7):
    model = MODEL_APIS.get(model_name)
    if not model:
        raise ValueError("Model not found in config")

    headers = {
        "Authorization": f"Bearer {model['key']}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": temperature
    }

    response = requests.post(model['url'], headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
