import json
import os

TASK_FILE = "automation/tasks.json"

os.makedirs("automation", exist_ok=True)


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def show_tasks():
    tasks = load_tasks()

    if not tasks:
        return "Tumhare paas koi task nahi hai."

    result = "Tumhare tasks:\n"

    for i, task in enumerate(tasks, 1):
        result += f"{i}. {task}\n"

    return result


def clear_tasks():
    save_tasks([])
    return "Saare tasks delete kar diye."
