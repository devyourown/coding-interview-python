from collections import defaultdict

def is_same_in_onetime(s1, s2):
    if len(s1) < len(s2):
        return is_same_in_onetime(s2, s1)
    if len(s1) - len(s2) > 1:
        return False
    alphas = defaultdict(int)
    for c in s1:
        alphas[c] += 1
    for c in s2:
        alphas[c] -= 1
    diff_alpha = 0
    for v in alphas.values():
        if v != 0:
            diff_alpha += 1
    if diff_alpha > 2:
        return False
    sum_of_values = sum(alphas.values())
    if 0 <= sum_of_values <= 1:
        return True
    return False

print(is_same_in_onetime('pale', 'ple'))
print(is_same_in_onetime('pales', 'pale'))
print(is_same_in_onetime('pale', 'bale'))
print(is_same_in_onetime('pale', 'bake'))
print(is_same_in_onetime('pale', 'xle'))