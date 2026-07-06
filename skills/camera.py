import os

def take_photo():
    path = "/sdcard/UlluAI_Photo.jpg"
    os.system(f"termux-camera-photo -c 0 {path}")
    return f"Photo le li hai. {path} me save kar di."
