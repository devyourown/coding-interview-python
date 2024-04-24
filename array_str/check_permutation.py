from collections import defaultdict

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    alphas = defaultdict(int)
    for c in s1:
        alphas[c] += 1
    for c in s2:
        if alphas[c] == 0:
            return False
        alphas[c] -= 1
    return True