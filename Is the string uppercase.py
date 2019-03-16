def is_uppercase(inp):
    arr = []
    for word in inp.split():
        for ch in word:
            arr.append(False if ch.islower() else True)
    return False if False in arr else True
