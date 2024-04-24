def is_sub_string(s1, s2):
    for i in range(len(s2) - len(s1) + 1):
        if s1 == s2[i:i+len(s1)]:
            return True
    return False

def is_rotated_str(s1, s2):
    if is_sub_string(s1, s2+s2):
        return True
    return False