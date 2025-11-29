def rabin_karp_search(text, pattern):

    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0
    if m > n:
        return -1

    base = 256
    mod = 10**9 + 7

    pattern_hash = 0
    window_hash = 0

    h = 1
    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i : i + m] == pattern:
                return i

        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * h) % mod
            window_hash = (window_hash * base) % mod
            window_hash = (window_hash + ord(text[i + m])) % mod
            if window_hash < 0:
                window_hash += mod
    return -1
