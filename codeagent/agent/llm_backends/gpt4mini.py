import requests

def call_gpt4mini(user_input):
    url = "http://localhost:8001/v1/chat/completions"  # Change as needed
    headers = {
        "Authorization": "Bearer your_gpt4mini_key"
    }
    payload = {
        "model": "gpt-4-mini",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }
    res = requests.post(url, headers=headers, json=payload)
    return res.json()["choices"][0]["message"]["content"]
