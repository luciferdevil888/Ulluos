import os
import time


def take_screenshot():
    filename = f"/sdcard/Pictures/Ullu_{int(time.time())}.png"

    os.system(f"termux-screenshot {filename}")

    return "Screenshot le liya."
