def find_even_index(arr):
    suma = sum(arr)
    lsuma, rsuma = 0, 0
    for index, x in enumerate(arr):
        rsuma=suma-x-lsuma
        if lsuma==rsuma:
            return index
        lsuma+=x
    return -1
