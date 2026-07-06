import asyncio
import edge_tts
import os

VOICE = "en-US-AriaNeural"

async def _speak(text):
    await edge_tts.Communicate(text, VOICE).save("voice.mp3")

def speak(text):
    print(f"Ullu: {text}")

    try:
        asyncio.run(_speak(text))
        os.system("mpv --no-video voice.mp3")
    except Exception as e:
        print("Voice Error:", e)
