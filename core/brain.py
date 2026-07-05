from phone.open_app import open_app
from skills.battery_skill import get_battery
from memory.memory import save_memory, read_memory
from skills.time_skill import get_time
from skills.date_skill import get_date
from skills.calculator_skill import calculate
import os


def reply(user):
    text = user.lower().strip()

    if text == "hello":
        return "Hello Lavibaby! ❤️"

    elif text == "hi":
        return "Hi Lavibaby! ❤️"

    elif text == "time":
        return get_time()

    elif text == "date":
        return get_date()

    elif text == "battery":
        return get_battery()

    elif text.startswith("calculate "):
        expression = user[10:]
        return calculate(expression)

    elif text.startswith("remember "):
        memory = user[9:]
        save_memory(memory)
        return "Theek hai, maine yaad rakh liya."

    elif text == "what do you remember":
        return read_memory()

    elif text == "torch on":
        os.system("termux-torch on")
        return "Torch on kar di."

    elif text == "torch off":
        os.system("termux-torch off")
        return "Torch off kar di."

    elif text.startswith("open "):
        app = text[5:]
        return open_app(app)

    else:
        return (
            "Mujhe abhi iska jawab nahi pata. "
            "Lekin main roz aur intelligent banti ja rahi hoon. 🦉"
        )
