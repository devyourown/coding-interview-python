def has_duplicated(s):
    alphas = {}
    for c in s:
        if c in alphas:
            return True
        alphas[c] = 1
    return False