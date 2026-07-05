import os

def open_app(app_name):
    app = app_name.lower().strip()

    commands = {
        "settings": "am start -a android.settings.SETTINGS",
        "wifi": "am start -a android.settings.WIFI_SETTINGS",
        "bluetooth": "am start -a android.settings.BLUETOOTH_SETTINGS",
        "display": "am start -a android.settings.DISPLAY_SETTINGS",
        "sound": "am start -a android.settings.SOUND_SETTINGS",
    }

    if app in commands:
        os.system(commands[app])
        return f"{app} open kar rahi hoon."

    return f"{app} ke liye command abhi available nahi hai."
