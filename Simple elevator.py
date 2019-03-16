def goto(level,button):
    if type(level).__name__!='int' or type(button).__name__!='str' or level>3 or int(button)>3:
        return 0
    return int(button) - level
