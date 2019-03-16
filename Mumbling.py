def accum(s):
    return "-".join([(ch*(index+1)).capitalize() for index, ch in enumerate(s)])
