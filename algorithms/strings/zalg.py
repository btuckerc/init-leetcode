def z_algorithm(s):
    z = [0] * len(s)
    l, r, k = 0, 0, 0
    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            while r < len(s) and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < len(s) and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z
