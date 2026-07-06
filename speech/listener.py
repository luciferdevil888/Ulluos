import os
import time
import speech_recognition as sr
from pydub import AudioSegment


def listen():
    print("🎤 Bolo...")

    audio_file = "voice.m4a"
    wav_file = "voice.wav"

    # Purani files delete karo
    for file in [audio_file, wav_file]:
        if os.path.exists(file):
            os.remove(file)

    # 5 second recording
    os.system(f"termux-microphone-record -f {audio_file} -l 5")

    # Recording complete hone ka wait
    time.sleep(6)

    recognizer = sr.Recognizer()

    try:
        audio = AudioSegment.from_file(audio_file)
        audio.export(wav_file, format="wav")

        with sr.AudioFile(wav_file) as source:
            data = recognizer.record(source)

        text = recognizer.recognize_google(data, language="en-IN")
        text = text.strip()

        print(f"🎤 Tum: {text}")

        return text

    except Exception as e:
        print("Voice Error:", e)
        return ""
