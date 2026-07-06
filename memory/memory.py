import os

MEMORY_FILE = "memory/data.txt"

# Folder bana do agar nahi hai
os.makedirs("memory", exist_ok=True)


def save_memory(text):
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")


def read_memory():
    if not os.path.exists(MEMORY_FILE):
        return "Mujhe abhi kuch yaad nahi hai."

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return "Mujhe abhi kuch yaad nahi hai."

    return "\n".join(lines)


def last_memory():
    if not os.path.exists(MEMORY_FILE):
        return ""

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return ""

    return lines[-1]


def search_memory(keyword):
    if not os.path.exists(MEMORY_FILE):
        return ""

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    keyword = keyword.lower()

    for line in reversed(lines):
        if keyword in line.lower():
            return line.strip()

    return ""
