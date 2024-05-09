import math

N = int(input())
num_of_candidate = list(map(int, input().split()))
chief, semi = map(int, input().split())

result = 0
for num in num_of_candidate:
    if chief >= num:
        result += 1
        continue
    needed_semi = math.ceil((num - chief) / semi)
    result += (needed_semi + 1)
print(result)