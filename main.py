import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("error")
    exit()

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data_payload = {
    "model": "deepseek/deepseek-chat-v3-0324:free",
    "messages": [{"role": "user", "content": "Explain why .gitignore is a developer's best friend. "}]
}
print("Sending final, upgraded request to OpenRouter AI..")

try:
    response = requests.post(API_URL, headers = headers, data = json.dumps(data_payload))
    response.raise_for_status()
    response_data = response.json()
    
    ai_answer = response_data['choices'][0]['message']['content']
    print("\nAI RESPONSE")
    print(ai_answer)

except requests.exceptions.RequestException as e:
    print(f"The API request failed {e}")
except (KeyError, IndexError):
    print("AI's response was a weird format. Couldn't find the answer")