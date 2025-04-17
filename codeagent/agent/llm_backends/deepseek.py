import requests

def call_deepseek(user_input):
    url = "http://localhost:8000/v1/chat/completions"  # Change as needed
    headers = {
        "Authorization": "Bearer your_deepseek_key"
    }
    payload = {
        "model": "deepseek-coder",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }
    res = requests.post(url, headers=headers, json=payload)
    return res.json()["choices"][0]["message"]["content"]
