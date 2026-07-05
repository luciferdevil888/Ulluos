from config.settings import APP_NAME, OWNER
from core.brain import reply
from speech.listener import listen
from voice.speaker import speak

print(f"Welcome to {APP_NAME}")
print(f"Owner: {OWNER}")

speak("Hello Lavibaby, Ullu AI is ready.")

while True:
    user = listen()

    if user.lower().strip() == "exit":
        speak("Bye Lavibaby!")
        break

    response = reply(user)
    speak(response)
