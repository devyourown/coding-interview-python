import copy

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
cache = {}
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
result = 11
def move(cur_state, d, next_board):
    ry, rx, by, bx = cur_state
    nry, nrx, nby, nbx = ry + d[0], rx + d[1], by + d[0], bx + d[1]
    while next_board[nby][nbx] == '.' or next_board[nry][nrx] == '.':
        if next_board[nry][nrx] == '.':
            next_board[nry][nrx], next_board[ry][rx] = next_board[ry][rx], next_board[nry][nrx]
            ry, rx = nry, nrx
            nry, nrx = nry + d[0], nrx + d[1]
        if next_board[nby][nbx] == '.':
            next_board[nby][nbx], next_board[by][bx] = next_board[by][bx], next_board[nby][nbx]
            by, bx = nby, nbx
            nby, nbx = nby + d[0], nbx + d[1]
    return ry, rx, by, bx, next_board


def dfs(red_y, red_x, blue_y, blue_x, cnt, cur_board):
    global result
    if cnt >= result:
        return
    for i, d in enumerate(direction):
        nry, nrx, nby, nbx, next_board = move((red_y, red_x, blue_y, blue_x), d, copy.deepcopy(cur_board))
        if next_board[nry+d[0]][nrx+d[1]] == 'O':
            if next_board[nby+d[0]][nbx+d[1]] == 'R':
                continue
            result = min(result, cnt + 1)
        elif next_board[nby+d[0]][nbx+d[1]] == 'O':
            continue
        else:
            if (nry, nrx, nby, nbx) in cache and cnt + 1 >= cache[(nry, nrx, nby, nbx)]:
                continue
            cache[(nry, nrx, nby, nbx)] = cnt + 1
            dfs(nry, nrx, nby, nbx, cnt + 1, next_board)

red = (-1, -1)
blue = (-1, -1)
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            red = (y, x)
        if board[y][x] == 'B':
            blue = (y, x)
cache[(red[0], red[1], blue[0], blue[1])] = 0
dfs(red[0], red[1], blue[0], blue[1], 0, board)
if result > 10:
    print(-1)
else:
    print(result)