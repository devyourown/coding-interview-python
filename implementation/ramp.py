def can_be_road(road):
    index = 1
    cur = road[0]
    floor = 0
    while index < len(road):
        next = road[index]
        floor += 1
        if abs(cur-next) > 1:
            return 0
        if cur > next:
            while floor < L:
                index += 1
                floor += 1
                if index >= len(road) or next != road[index]:
                    return 0
            floor = 0
            continue
        elif cur < next:
            if floor < L:
                return 0
            floor = 0
        cur = road[index]
        index += 1
    return 1


N, L = map(int, input().split())
result = 0
column_road = [[] for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().split()))
    if can_be_road(row) or can_be_road(row[::-1]):
        print(*row)
        result += 1
    for i, val in enumerate(row):
        column_road[i].append(val)
for i in range(N):
    if can_be_road(column_road[i]) or can_be_road(column_road[i][::-1]):
        print(*column_road[i])
        result += 1
print(result)