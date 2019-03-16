def square_digits(num):
    return int(''.join([str(int(ch)**2) for ch in str(num)]))
