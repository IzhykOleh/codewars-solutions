def digital_root(n):
    if len(str(n))==1:
        return n
    else:
        n = sum([int(ch) for ch in str(n)])
        return digital_root(n)
