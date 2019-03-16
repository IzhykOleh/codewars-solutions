import re
def count_smileys(arr):
    counter = 0
    if arr:
        for i in arr:
            obj = re.match(r'(?:\:|;)(?:-|~)?(?:D|\))', i)
            if obj: counter+=1
        return counter
    else:
        return 0
