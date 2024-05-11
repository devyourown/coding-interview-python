from collections import deque

result = []
for _ in range(int(input())):
    s = input()
    differ = set()
    for c in s:
        differ.add(c)
        if len(differ) > 1:
            break
    if len(differ) == 1:
        result.append('NO')
        continue
    result.append('YES')
    temp = deque(s)
    while temp[0] == s[0]:
        temp.append(temp.popleft())
    result.append("".join(temp))
print(*result, sep="\n")

