import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise SystemExit("Set OPENROUTER_API_KEY in a .env file")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(message, system_prompt=None, model="openrouter/auto"):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": message})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 200,
        "temperature": 0.3
    }

    resp = requests.post(API_URL, json=payload, headers=headers, timeout=20)
    resp.raise_for_status()
    return resp.json()