def gimme(input_array):
    input_array_orig = input_array.copy()
    input_array.sort()
    return input_array_orig.index(input_array[1])
