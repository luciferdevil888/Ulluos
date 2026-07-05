from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"


def ask_gemini(prompt):
    if not API_KEY:
        return "Gemini API key nahi mili."

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Gemini Error: {e}"
