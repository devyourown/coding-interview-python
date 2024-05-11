result = []
for _ in range(int(input())):
    r = int(input())
    square = r ** 2
    plus_square = (r + 1) ** 2
    count = 0
    y = 0
    while y <= r:
        x = int((square - y ** 2) ** 0.5)
        count += x
        y += 1
    result.append(count * 4)
print(*result, sep="\n")