def find_outlier(integers):
    suma = sum([integers[i]%2 for i in range(3)])
    if suma>=2:
        return filter(lambda x: True if x%2==0 else False, integers)[0]
    else:
        return filter(lambda x: True if x%2!=0 else False, integers)[0]
