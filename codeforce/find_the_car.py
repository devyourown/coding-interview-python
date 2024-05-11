for _ in range(int(input())):
    n, k, q = map(int, input().split())
    points = list(map(int, input().split()))
    minutes = list(map(int, input().split()))
    for _ in range(q):
        asked = int(input())