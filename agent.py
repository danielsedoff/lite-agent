import json
import os
import requests
import sys

BASE_URL = "http://localhost:41637/v1"
MODEL_NAME = "<your-model-name>.gguf" # Name used when starting the server or full path
CONTEXT_FILE = "context.json"

def get_initial_context():
    #return [{"role": "system", "content": "You are a professional coding assistant."}]
    return [{"role": "system", "content": "Brief answers. Only code or math, minimum talk. Only certain knowledge."}]

def load_context():
    if os.path.exists(CONTEXT_FILE):
        try:
            with open(CONTEXT_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return get_initial_context()
    return get_initial_context()

def save_context(context):
    with open(CONTEXT_FILE, 'w', encoding='utf-8') as f:
        json.dump(context, f, indent=4)

def compile_payload(context):
    return ({
        "model": MODEL_NAME,
        "messages": context,
        "stream": False, # Set to true for streaming responses
        "temperature": 0.1
    })

user_input = " ".join(sys.argv[1:])

if not user_input.strip():
    print("No commandline arguments. Query is expected in commandline arguments.")
    print("arg0: clear -- clear context and quit.")
    sys.exit()

if user_input.lower() == "clear":
    if os.path.exists(CONTEXT_FILE):
        os.remove(CONTEXT_FILE)
    print("context cleared. quitting.")
    sys.exit()

context = load_context()
context.append({"role": "user", "content": user_input})

try:
    response = requests.post(f"{BASE_URL}/chat/completions", json=compile_payload(context))
    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print(f"\nLLM: {reply}")
        context.append({"role": "assistant", "content": reply})
        save_context(context)
    else:
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"Connection Error: {e}")


