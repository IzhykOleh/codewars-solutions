import re
def high_and_low(numbers):
    mas = [int(num) for num in re.findall(r'[-]?\d+', numbers)]
    return " ".join([str(i) for i in [max(mas), min(mas)]])
