MEMORY_FILE = "memory/data.txt"

def save_memory(text):
    with open(MEMORY_FILE, "a") as f:
        f.write(text + "\n")

def read_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            data = f.read().strip()
            if data:
                return data
            return "Mujhe abhi kuch yaad nahi hai."
    except FileNotFoundError:
        return "Mujhe abhi kuch yaad nahi hai."

def last_memory():
    data = read_memory()
    if data == "Mujhe abhi kuch yaad nahi hai.":
        return ""
    return data.split("\n")[-1]
