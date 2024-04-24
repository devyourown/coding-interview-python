def make_url(string, size):
    result = []
    for c in string:
        if c == ' ':
            result.append('%20')
        else:
            result.append(c)
    return ''.join(result)