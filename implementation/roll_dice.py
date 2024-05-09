N, M, y, x, k = map(int, input().split())
roll_map = []
for _ in range(N):
    roll_map.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
direction = [(0,0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [[0 for _ in range(3)]  for _ in range(4)]
pos = 1
result = []
for command in commands:
    dy, dx = direction[command]
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < M:
        opposite = (pos + 2) % 4
        npy = (pos + dy + 4) % 4
        if command == 1:
            left, right = dice[pos][1], dice[opposite][1]
            dice[pos][1] = dice[pos][2]
            dice[opposite][1] = dice[pos][0]
            dice[pos][0], dice[pos][2] = left, right
            result.append(dice[opposite][1])
        elif command == 2:
            left, right = dice[opposite][1], dice[pos][1]
            dice[pos][1] = dice[pos][0]
            dice[opposite][1] = dice[pos][2]
            dice[pos][0], dice[pos][2] = left, right
            result.append(dice[opposite][1])
        else:
            left, right = dice[pos][0], dice[pos][2]
            dice[npy][0], dice[npy][2] = left, right
            pos = npy
            opposite = (pos + 2) % 4
            result.append(dice[opposite][1])
        if roll_map[ny][nx] == 0:
            roll_map[ny][nx] = dice[pos][1]
        else:
            dice[pos][1] = roll_map[ny][nx]
            roll_map[ny][nx] = 0
        y, x = ny, nx
if result:
    print(*result, sep='\n')
