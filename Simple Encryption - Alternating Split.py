def decrypt(encrypted_text, n):
    for i in range(n):
        index = len(encrypted_text)/2
        if len(encrypted_text)%2!=0:
            flag = True
            index = int(index)
        else:
            flag = False
            index = int(index)
        second = encrypted_text[:index]
        first = encrypted_text[index:]
        res=""
        for x,y in zip(first, second):
            res+=(x+y)
        if flag:
            res+=first[-1]
        encrypted_text = res
    return encrypted_text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2]+text[::2]
    return text
