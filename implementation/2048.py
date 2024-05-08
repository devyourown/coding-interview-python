N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
incremental = [(1, N, 1, 0, N, 1), (N-2, -1, -1, 0, N, 1),
               (0, N, 1, 1, N, 1), (0, N, 1, N-2, -1, -1)]

def move(next_board, d_index):
    dy, dx = directions[d_index]
    sy, ey, ny, sx, ex, nx = incremental[d_index]
    flag = set()
    for y in range(sy, ey, ny):
        for x in range(sx, ex, nx):
            new_y, new_x = y + dy, x + dx
            while 0 <= new_y < N and 0 <= new_x < N and next_board[new_y][new_x] == 0:
                if next_board[new_y-dy][new_x-dx] == 0:
                    break
                next_board[new_y][new_x] = next_board[new_y-dy][new_x-dx]
                next_board[new_y-dy][new_x-dx] = 0
                new_y, new_x = new_y + dy, new_x + dx
            if not (0 <= new_y < N) or not (0 <= new_x < N):
                new_y, new_x = new_y - dy, new_x - dx
            if (new_y, new_x) not in flag and next_board[new_y][new_x] !=0 and \
                    next_board[new_y][new_x] == next_board[new_y-dy][new_x-dx]:
                next_board[new_y][new_x] *= 2
                next_board[new_y-dy][new_x-dx] = 0
                flag.add((new_y, new_x))


def dfs(cur_board, cnt):
    if cnt == 5:
        result = 0
        for cur in cur_board:
            result = max(result, max(cur))
        return result
    result = 0
    for i in range(4):
        next_board = [cur[:] for cur in cur_board]
        move(next_board, i)
        result = max(result, dfs(next_board, cnt + 1))
    return result

print(dfs(board, 0))
