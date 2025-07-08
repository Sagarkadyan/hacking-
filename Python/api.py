import requests
import json

token = "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"  # Replace with your actual API key
hello = """
 
"""

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
#print(response)
ai_response = response['choices'][0]['message']['content']
print(ai_response)  # Clean output (e.g., "The result of 2 + 2 is 4. 😊")
