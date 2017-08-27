def differentSquares(matrix):
    squares = set()
    for row in range(len(matrix) - 1):
        for cell in range(len(matrix[row]) - 1):
            square = ((matrix[row][cell], matrix[row][cell + 1]),
                      (matrix[row + 1][cell], matrix[row + 1][cell + 1]))
            squares.add(square)
    return len(squares)
