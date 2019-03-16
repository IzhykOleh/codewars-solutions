import re
def pig_it(text):
    return " ".join([(word[1:]+word[0]+"ay") if not(word=="?" or word=="!") else word for word in text.split() if word])
