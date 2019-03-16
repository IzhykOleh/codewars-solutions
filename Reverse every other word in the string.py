def reverse_alternate(string):
    string = string.strip()
    li = []
    for index, word in enumerate(string.split()): 
        if index%2!=0:
            li.append(word[::-1])
        else:
            li.append(word)
    return " ".join(li)
