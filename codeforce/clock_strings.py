result = []
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if c > d:
        c, d = d, c
    if (c < b < d and not (c < a < d)) or (c < a < d and not (c < b < d)):
        result.append('YES')
    else:
        result.append('NO')
print(*result, sep='\n')