def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    list_str = [i for i in string if not i in vowels]
    return ''.join(list_str)
