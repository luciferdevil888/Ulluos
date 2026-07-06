from skills.camera import open_camera
from skills.media import play_pause, pause, stop, info
from skills.volume import volume_up, volume_down, volume_half, volume_mute
from skills.browser import open_website, google_search
from skills.youtube_search import youtube_search
from skills.google_search import google_search
from ai.gemini import ask_gemini
from phone.open_app import open_app
from skills.battery_skill import get_battery
from memory.memory import save_memory, read_memory, search_memory
from skills.time_skill import get_time
from skills.date_skill import get_date
from skills.calculator_skill import calculate
import os


def reply(user):
    text = user.lower().strip()

    # ---------------- Greetings ----------------

    if text in ["hello", "hi", "hey", "hello ullu", "hey ullu", "hi ullu"]:
        return "Hello Lavibaby ❤️"

    elif "how are you" in text:
        return "Main bilkul theek hoon ❤️"

    elif "good morning" in text:
        return "Good Morning Lavibaby ☀️"

    elif "good night" in text:
        return "Good Night Lavibaby 🌙"

    # ---------------- Skills ----------------

    elif "time" in text:
        return get_time()

    elif "date" in text:
        return get_date()

    elif "battery" in text:
        return get_battery()

    elif text.startswith("calculate "):
        return calculate(user[10:])

    # ---------------- Google Search ----------------

    elif text.startswith("search "):
        return google_search(user[7:])

    elif text.startswith("google "):
        return google_search(user[7:])

    elif "search for" in text:
        query = user.lower().replace("search for", "").strip()
        return google_search(query)

    # ---------------- Browser ----------------

    elif text.startswith("search "):
        return google_search(user[7:])

    elif text.startswith("google "):
        return google_search(user[7:])

    elif text.startswith("open website "):
        return open_website(user[13:])

    elif text.startswith("open github"):
        return open_website("github.com")

    elif text.startswith("open google"):
        return open_website("google.com")

    elif text.startswith("open amazon"):
        return open_website("amazon.in")

    elif text.startswith("open openai"):
        return open_website("openai.com")

    elif text.startswith("open wikipedia"):
        return open_website("wikipedia.org")

    # ---------------- Memory ----------------

    elif "my favourite game is" in text:
        game = user.split("is", 1)[1].strip()
        save_memory(f"Favourite Game: {game}")
        return f"Theek hai, favourite game {game} yaad rakh liya."

    elif "my favourite color is" in text:
        color = user.split("is", 1)[1].strip()
        save_memory(f"Favourite Color: {color}")
        return f"Theek hai, favourite color {color} yaad rakh liya."

    elif "what is my favourite game" in text:
        ans = search_memory("Favourite Game")
        return ans if ans else "Mujhe yaad nahi."

    elif "what is my favourite color" in text:
        ans = search_memory("Favourite Color")
        return ans if ans else "Mujhe yaad nahi."

    elif text.startswith("remember "):
        save_memory(user[9:])
        return "Yaad rakh liya."

    elif "what do you remember" in text:
        return read_memory()

    # ---------------- Torch ----------------

    elif "torch on" in text:
        os.system("termux-torch on")
        return "Torch on kar di."

    elif "torch off" in text:
        os.system("termux-torch off")
        return "Torch off kar di."

    # ---------------- Open Apps ----------------

    elif "youtube" in text:
        return open_app("youtube")

    elif "whatsapp" in text:
        return open_app("whatsapp")

    elif "chrome" in text:
        return open_app("chrome")

    elif "chatgpt" in text:
        return open_app("chatgpt")

    elif "telegram" in text:
        return open_app("telegram")

    elif "camera" in text or "open camera" in text:
        return open_camera()

    # ---------------- Volume ----------------

    elif "volume up" in text:
        return volume_up()

    elif "volume down" in text:
        return volume_down()

    elif "volume half" in text:
        return volume_half()

    elif "mute" in text:
        return volume_mute()

    # ---------------- Media ----------------

    elif "play music" in text:
        return play_pause()

    elif "pause music" in text:
        return pause()

    elif "stop music" in text:
        return stop()

    elif "media info" in text:
        return info()

    elif text.startswith("play "):
        return youtube_search(user[5:])

    elif text.startswith("youtube "):
        return youtube_search(user[8:])

    elif text.startswith("watch "):
        return youtube_search(user[6:])

    # ---------------- AI ----------------

    else:
        return ask_gemini(user)
