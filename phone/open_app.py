import os

SYSTEM_COMMANDS = {
    "settings": "am start -a android.settings.SETTINGS",
    "wifi": "am start -a android.settings.WIFI_SETTINGS",
    "bluetooth": "am start -a android.settings.BLUETOOTH_SETTINGS",
    "display": "am start -a android.settings.DISPLAY_SETTINGS",
    "sound": "am start -a android.settings.SOUND_SETTINGS",
}

APP_COMMANDS = {
    "youtube": "am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity",
    "whatsapp": "am start -n com.whatsapp/.HomeActivity",
    "chrome": "am start -n com.android.chrome/com.google.android.apps.chrome.Main",
    "chatgpt": "am start -n com.openai.chatgpt/.MainActivity",
    "telegram": "am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity",
}


def open_app(text):

    text = text.lower()

    commands = [
        "open",
        "kholo",
        "khol do",
        "start",
        "launch",
        "chalu karo",
        "open the"
    ]

    app = text

    for cmd in commands:
        app = app.replace(cmd, "")

    app = app.strip()

    if app in SYSTEM_COMMANDS:
        os.system(SYSTEM_COMMANDS[app])
        return f"{app} open kar rahi hoon."

    if app in APP_COMMANDS:
        os.system(APP_COMMANDS[app])
        return f"{app} open kar rahi hoon."

    return f"{app} mujhe nahi mila."
