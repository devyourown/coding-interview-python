result = []
for _ in range(int(input())):
    binary = input()
    piece = 1
    cur = binary[0]
    for b in binary[1:]:
        if cur > b:
            cur = b
            piece += 1
        cur = b
    result.append(piece)
print(*result, sep="\n")