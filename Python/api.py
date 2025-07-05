import requests
import json

token = "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"  # Replace with your actual API key
hello = input("Enter the text: ")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {
                "role": "user",
                "content": hello
            }
        ],
    })
).json()  # Parse JSON response directly

# Extract and print ONLY the AI's response
ai_response = response['choices'][0]['message']['content']
print(ai_response)  # Clean output (e.g., "The result of 2 + 2 is 4. 😊")
