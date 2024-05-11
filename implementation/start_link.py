import sys
from itertools import combinations

input = sys.stdin.readline


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
players = [i for i in range(N)]
result = 987654321
for team in combinations(players, N//2):
    joined = set(team)
    start = 0
    link = 0
    for i in range(N):
        for j in range(i + 1, N):
            if i in joined and j in joined:
                start += board[i][j] + board[j][i]
            elif i not in joined and j not in joined:
                link += board[i][j] + board[j][i]
    result = min(result, abs(start-link))
print(result)

