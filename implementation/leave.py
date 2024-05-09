def do_job(index):
    if index > N:
        return -987654321
    if index == N:
        return 0
    if index in cache:
        return cache[index]
    day, money = counsel[index]
    ret = max(money + do_job(index+day), do_job(index+1))
    cache[index] = ret
    return ret

N = int(input())
counsel = []
cache = {}
for _ in range(N):
    counsel.append(map(int, input().split()))
print(do_job(0))