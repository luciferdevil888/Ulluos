import os
from phone.apps import APPS

SYSTEM_COMMANDS = {
    "settings": "am start -a android.settings.SETTINGS",
    "wifi": "am start -a android.settings.WIFI_SETTINGS",
    "bluetooth": "am start -a android.settings.BLUETOOTH_SETTINGS",
    "display": "am start -a android.settings.DISPLAY_SETTINGS",
    "sound": "am start -a android.settings.SOUND_SETTINGS",
}

def open_app(app_name):
    app = app_name.lower().strip()

    if app in SYSTEM_COMMANDS:
        os.system(SYSTEM_COMMANDS[app])
        return f"{app} open kar rahi hoon."

    if app in APPS:
        package = APPS[app]
        os.system(f"monkey -p {package} -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1")
        return f"{app} open kar rahi hoon."

    return f"'{app}' mujhe nahi mila."
