def remove_smallest(numbers):
    n = numbers.copy()
    try:
        n.remove(min(n))
    except ValueError:
        return []
    return n
