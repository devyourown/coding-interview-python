def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            result[n-1-x][y] = matrix[y][x]
    return result

def rotate_matrix_without(matrix):
    n = len(matrix)
    for y in range(n//2):
        for x in range(math.ceil(n/2)):
            matrix[y][x], matrix[n-1-x][y], matrix[n-1+y][n-1+x], matrix[x][n-1-y] = \
            matrix[x][n-1-y], matrix[y][x], matrix[n-1-x][y], matrix[n-1+y][n-1+x]
    return matrix