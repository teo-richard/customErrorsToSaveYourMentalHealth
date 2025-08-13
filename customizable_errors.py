import sys

def emoji_excepthook(exc_type, exc_value, exc_traceback):
    print("🍆💦🌹➡️🥀 Error: You can't do that shih here vro")


sys.excepthook = emoji_excepthook

