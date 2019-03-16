def show_sequence(n):
    if n==0: return "0=0"
    if n<0: return "%i<0" %n
    a = list(range(n+1))
    b = [str(i) for i in a]
    return "+".join(b) + " = " + str(sum(a))
