import os


def volume_up():
    os.system("termux-volume music 15")
    return "Volume full kar diya."


def volume_down():
    os.system("termux-volume music 5")
    return "Volume kam kar diya."


def volume_half():
    os.system("termux-volume music 8")
    return "Volume aadha kar diya."


def volume_mute():
    os.system("termux-volume music 0")
    return "Volume mute kar diya."
