def in_array(ar1, ar2):
    return sorted(list(set(x for x in ar1 for y in ar2 if y.find(x)!=-1)))
