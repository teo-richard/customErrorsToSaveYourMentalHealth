import sys
import json
import random
from dictionary_of_themes import THEMES as DEFAULT_THEMES 

class ErrorHandler:
    def __init__(self, 
                 message=None, 
                 theme_name=None,
                 theme=None,
                 custom_themes=None,
                 theme_mode ="default",
                 want_original=False):
        
        self.message = message or "🍆🍆🍆🍆🍆🍆 ur mom is so beautiful"
        self.theme_mode = theme_mode
        self.theme_name = theme_name

        self.want_original = want_original
        self.original_hook = sys.__excepthook__

        if self.theme_mode == "default":
            self.theme = DEFAULT_THEMES

        elif self.theme_mode == "custom":
            if custom_themes is None:
                print("you have no custom themes loser. you get the default ones.")
                self.theme = DEFAULT_THEMES
            else:
                self.theme = custom_themes

        elif self.theme_mode == "both":
            if custom_themes is None:
                print("you have no custom themes loser. you get the default ones.")
                self.theme = DEFAULT_THEMES
            else:
                self.theme = DEFAULT_THEMES.copy()
                for key, messages in custom_themes.items():
                    if key in self.theme:
                        self.theme[key] += messages
                    else:
                        self.theme[key] = messages
            
        else:
            print("idk what the FUCK you put in to get this but you get default themes")
            self.theme = DEFAULT_THEMES

    def __call__(self, exc_type, exc_value, exc_traceback):
        bad_theme = False
        if self.theme_name is None:
            print(f"{self.message}")
        elif self.theme_name == "random":
            key = random.choice(list(self.theme.keys()))
            msg = random.choice(self.theme[key])
            print(msg)
        else:
            if self.theme_name in self.theme:
                msg = random.choice(self.theme[self.theme_name])
                print(msg)
            else:
                bad_theme = True
                print(f"Theme {self.theme_name} not found fuckhead")
                print("This is the original excepthook bc u can't figure out how to put the theme in properly:")
                self.original_hook(exc_type, exc_value, exc_traceback)
        if self.want_original and bad_theme != True:
            self.original_hook(exc_type, exc_value, exc_traceback)
 




#sys.excepthook = ErrorHandler(theme_name="random", theme_mode = "both")

#1/0
