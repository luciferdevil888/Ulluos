import os


def open_camera():
    os.system(
        "am start -n com.motorola.camera3/com.motorola.camera.Camera"
    )
    return "Camera open kar rahi hoon."
