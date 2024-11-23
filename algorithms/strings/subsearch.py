def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i : i + m]) == p_hash and text[i : i + m] == pattern:
            return i
    return -1
