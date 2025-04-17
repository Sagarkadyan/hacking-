import json
import os

HISTORY_FILE = "chat_history.json"

def save_history(entry):
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w') as f:
            json.dump([], f)

    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)

    history.append(entry)

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)
