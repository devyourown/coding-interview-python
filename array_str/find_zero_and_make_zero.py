def find_zero(matrix):
    result = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                result.append((y, x))
    return result

def make_it_zero(matrix, zeros):
    for (y, x) in zeros:
        for row in len(matrix[0]):
            matrix[y][row] = 0
        for column in len(matrix):
            matrix[column][x] = 0

def find_zero_and_make_zero(matrix):
    zeros = find_zero(matrix)
    make_it_zero(matrix, zeros)
    return matrix