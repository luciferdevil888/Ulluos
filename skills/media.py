import os


def play_pause():
    os.system("termux-media-player play")
    return "Media play kar rahi hoon."


def pause():
    os.system("termux-media-player pause")
    return "Media pause kar diya."


def stop():
    os.system("termux-media-player stop")
    return "Media stop kar diya."


def info():
    os.system("termux-media-player info")
    return "Media information check kar rahi hoon."
