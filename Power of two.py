def power_of_two(x):
    a = 1
    while a < x:
        a*=2
    return True if x-a==0 else False
