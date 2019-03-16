def tribonacci(sig, n):
    if not n: return []
    if n<3: return sig[:n]
    s = sig.copy()
    s.extend((sum(s[-3:]) for x in range(n-3)))
    return s
