def compress(s):
    result = []
    prev = s[0]
    size = 1
    for c in s[1:]:
        if prev != c:
            result.append(prev + str(size))
            size = 1
            prev = c
        else:
            size += 1
    result.append(prev + str(size))
    compressed = ''.join(result)
    if len(compressed) > len(s):
        return s
    return compressed