import json
import os
import requests
import sys
from get_model import get_active_model_port
from args_as_text import args_as_text

CONTEXT_FILE = "context.json"
print("agent starting. arg1=clear: clear context and quit.")

good_port = get_active_model_port()
base_url = f"http://localhost:{good_port}/v1"

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
        "model": "LOCAL MODEL",
        "messages": context,
        "stream": False, # Set to true for streaming responses
        "temperature": 0.1
    })

user_input = args_as_text()

if user_input.lower() == "clear":
    if os.path.exists(CONTEXT_FILE):
        os.remove(CONTEXT_FILE)
    print("context cleared. quitting.")
    sys.exit()

context = load_context()
context.append({"role": "user", "content": user_input})

try:
    response = requests.post(f"{base_url}/chat/completions", json=compile_payload(context))
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
