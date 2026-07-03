from memory.memory import save_memory, read_memory
from skills.time_skill import get_time
from skills.date_skill import get_date
from skills.calculator_skill import calculate
from skills.time_skill import get_time
from skills.date_skill import get_date
from memory.memory import save_memory, read_memory
from skills.time_skill import get_time
from memory.memory import save_memory, read_memory

def reply(user):
    user = user.lower().strip()

    if user == "hello":
        return "Hello Lavibaby! ❤️"

    elif user == "hi":
        return "Hi Lavibaby!"

    elif user == "kaise ho":
        return "Main bilkul theek hoon."

    elif user == "tum kon ho":
        return "Main Ullu AI hoon. Tumhari personal AI assistant."

    elif user == "owner":
        return "Mere owner Lavibaby hain."

    elif user == "time":
        return "Abhi ka time hai " + get_time()

    elif user == "date":
        return "Aaj ki date hai " + get_date()

    elif user.startswith("remember "):
        text = user.replace("remember ", "")
        save_memory(text)
        return "Theek hai, maine yaad rakh liya."

    elif user == "what do you remember":
        return read_memory()

    elif user == "bye":
        return "Bye Lavibaby! Jaldi milte hain."

    elif user.startswith("calculate "):
        expression = user.replace("calculate ", "")
        return "Answer: " + calculate(expression)

    else:
        return "Mujhe abhi ye command nahi aati."
