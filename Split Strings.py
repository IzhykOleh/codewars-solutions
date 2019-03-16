import re
def solution(s):
    return [p+"_" if len(p)==1 else p for p in re.split(r'(\w\w)', s) if p]
