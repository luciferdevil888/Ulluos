import os

def speak(text):
    print(f"Ullu: {text}")

    try:
        safe_text = text.replace("Lavibaby", "Lavi baby").replace('"', '\\"')
        os.system(f'termux-tts-speak "{safe_text}"')
    except Exception:
        pass
