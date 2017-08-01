def minesweeper(matrix):
    TOP = 0
    BOTTOM = len(matrix) - 1
    LEFT = 0
    RIGHT = len(matrix[0]) - 1

    outMatrix = []
    for row in range(len(matrix)):
        outRow = []
        for cell in range(len(matrix[row])):
            outRow.append(0)
            if row != TOP:
                outRow[cell] += matrix[row - 1][cell]
            if row != BOTTOM:
                outRow[cell] += matrix[row + 1][cell]
            if cell != LEFT:
                outRow[cell] += matrix[row][cell - 1]
            if cell != RIGHT:
                outRow[cell] += matrix[row][cell + 1]
            if row != TOP and cell != LEFT:
                outRow[cell] += matrix[row - 1][cell - 1]
            if row != TOP and cell != RIGHT:
                outRow[cell] += matrix[row - 1][cell + 1]
            if row != BOTTOM and cell != LEFT:
                outRow[cell] += matrix[row + 1][cell - 1]
            if row != BOTTOM and cell != RIGHT:
                outRow[cell] += matrix[row + 1][cell + 1]
        outMatrix.append(outRow)
    return outMatrix
