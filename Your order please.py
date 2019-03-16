def order(s):
    return ' '.join(sorted(s.split(), key = lambda x: [i for i in x if i.isdigit()]))
