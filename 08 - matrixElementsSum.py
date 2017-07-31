def matrixElementsSum(matrix):
    if len(matrix) > 1:
        for row in range(1, len(matrix)):
            for room in range(len(matrix[row])):
                if matrix[row - 1][room] == 0:
                    matrix[row][room] = 0
    sum = 0
    for row in matrix:
        for room in row:
            sum += room
    return sum
