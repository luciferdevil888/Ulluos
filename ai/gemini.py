from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

session = requests.Session()


def ask_gemini(prompt):
    if not API_KEY:
        return "Gemini API key nahi mili."

    try:
        response = session.post(
            URL,
            params={"key": API_KEY},
            json={
                "system_instruction": {
                    "parts": [
                        {
                            "text": (
                                "You are Ullu. "
                                "You are a smart, caring and natural female AI assistant. "
                                "The user's name is Lavibaby. "
                                "Always call the user Lavibaby naturally. "
                                "Speak in Hinglish unless the user asks for another language. "
                                "Be warm, friendly, caring and never robotic. "
                                "Keep replies short (1-3 sentences) unless the user asks for details. "
                                "Help Lavibaby build Ullu AI OS. "
                                "If you don't know something, say so honestly."
                            )
                        }
                    ]
                },
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.9,
                    "maxOutputTokens": 150
                }
            },
            timeout=(10, 60)
        )

        response.raise_for_status()

        data = response.json()

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]

        return "Mujhe koi response nahi mila."

    except requests.exceptions.Timeout:
        return "Internet ya Gemini server slow hai. Dobara try karo."

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            return "Gemini ki request limit khatam ho gayi hai. Thodi der baad dobara try karo."
        elif e.response.status_code == 503:
            return "Gemini server abhi busy hai. Thodi der baad try karo."
        return f"HTTP Error: {e}"

    except Exception as e:
        return f"Gemini Error: {e}"
