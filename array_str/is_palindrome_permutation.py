from collections import defaultdict

def is_palindrome_permutation(s: str):
    s = ''.join([c if c.isalpha() else '' for c in s])
    has_one_odd = False
    alphas = defaultdict(int)
    for c in s:
        alphas[c] += 1
    for c in s:
        if alphas[c] % 2 == 1:
            if has_one_odd:
                return False
            has_one_odd = True
    return True