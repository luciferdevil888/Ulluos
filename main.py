from config.settings import APP_NAME, OWNER
from core.brain import reply

print(f"Welcome to {APP_NAME}")
print(f"Owner: {OWNER}")

print("Ullu: Hello Lavibaby, Ullu AI is ready.")

while True:
    user = input("Tum: ")

    if user.lower().strip() == "exit":
        print("Ullu: Bye Lavibaby!")
        break

    response = reply(user)
    print("Ullu:", response)
