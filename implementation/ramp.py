def can_be_road(road):
    ramp = [False] * N
    for i in range(1, N):
        if abs(road[i-1]-road[i]) > 1:
            return False
        elif road[i-1] - road[i] == 1:
            for j in range(L):
                if i + j >= N:
                    return False
                elif road[i] != road[i+j]:
                    return False
                elif ramp[i+j]:
                    return False
                ramp[i+j] = True
        elif road[i-1] - road[i] == -1:
            for j in range(L):
                if i-1-j < 0:
                    return False
                elif road[i-1] != road[i-1-j]:
                    return False
                elif ramp[i-1-j]:
                    return False
                ramp[i-1-j] = True
    return True


N, L = map(int, input().split())
result = 0
column_road = [[] for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().split()))
    if can_be_road(row):
        result += 1
    for i, val in enumerate(row):
        column_road[i].append(val)
for i in range(N):
    if can_be_road(column_road[i]):
        result += 1
print(result)