import string
def find_missing_letter(chars):
    s = string.ascii_lowercase if chars[0].islower() else string.ascii_uppercase
    sb = s[s.find(chars[0]) : s.find(chars[-1])+1]
    return list(set(sb)-set(chars))[0]
