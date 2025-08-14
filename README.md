1. Import
    ```python
    from customErrorMessagesToSaveYourMentalHealth import ErrorHandler
    import sys
    ```

* (Optional) Import your custom themes
    * Note: these must be as a dictionary structured like so:
        ```python
        my_custom_themes = {"happy": ["happy message 1", "happy message 2"],
                            "goofy": ["goofy message 1", "goofy message 2", "goofy message 3"]}
        ```
    * To import:
        ```python
        from my_file_containing_my_themes import my_custom_themes
        ```

2. Basic structure
    ```python
    sys.excepthook = ErrorHandler(message=None, 
                    theme_name=None,
                    theme=None,
                    custom_themes=None,
                    theme_mode ="default",
                    want_original=False)
    ```

    Example:
    ```python
    sys.excepthook = ErrorHandler(theme_name="random", 
                        custom_themes=my_custom_themes,
                        theme_mode="custom")
    ```
    This will select random themes from only your custom themes.

Parameters: \
`message` - The message you want to write out if you don't want to pick a themed message \
`theme_name` - The name of the theme e.g. `"romance"` (Only a few are supported right now because I have a life outside of this stupid crap) \
`theme` - ignore this it probably doesn't have to be a parameter tbh \
`custom_themes` - set this equal to your custom themes if you got any
`theme_mode` - `"default"`, `"custom"`, or `"both"` \
`want_original` - if you want the original error (it'll give you `__excepthook__`)

If you are illiterate and don't put things in correctly the code will be mean to you and then default to the default themes. 