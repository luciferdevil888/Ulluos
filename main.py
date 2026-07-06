from config.settings import APP_NAME, OWNER
from core.brain import reply
from speech.listener import listen
from voice.speaker import speak
import time

print(f"Welcome to {APP_NAME}")
print(f"Owner: {OWNER}")

speak("Hello Lavibaby, Ullu AI is ready.")

activated = False
last_command_time = 0

while True:
    user = listen()

    if not user:
        continue

    text = user.lower().strip()

    # Wake word
    if not activated:
        if "hey ullu" in text or text == "ullu":
            activated = True
            last_command_time = time.time()
            speak("Ji Lavibaby, main sun rahi hoon.")
        continue

    # Exit
    if "bye" in text or "exit" in text:
        speak("Bye Lavibaby!")
        break

    # Normal command
    response = reply(user)
    speak(response)

    last_command_time = time.time()

    # Continuous conversation (30 seconds)
    while True:
        if time.time() - last_command_time > 30:
            activated = False
            speak("Main standby mode mein ja rahi hoon.")
            break

        user = listen()

        if not user:
            continue

        text = user.lower().strip()

        if "bye" in text or "exit" in text:
            speak("Bye Lavibaby!")
            exit()

        response = reply(user)
        speak(response)

        last_command_time = time.time()
