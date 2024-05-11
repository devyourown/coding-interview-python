result = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        result.append(str(x) + ' ' + str(y))
    else:
        result.append(str(y) + ' ' + str(x))
print(*result, sep='\n', end='\n')