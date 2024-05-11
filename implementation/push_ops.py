N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
result = [-1987654321, 1987654321]


def calc(i, left, right):
    if i == 0:
        return left + right
    elif i == 1:
        return left - right
    elif i == 2:
        return left * right
    else:
        if left < 0:
            return -(-left // right)
        return left // right


def solve(index, ret, ops):
    if index == N:
        result[0] = max(result[0], ret)
        result[1] = min(result[1], ret)
        return
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            calculated = calc(i, ret, nums[index])
            solve(index+1, calculated, ops)
            ops[i] += 1


solve(1, nums[0], op)
print(result[0])
print(result[1])