def sudoku(grid):
    match = [i for i in range(1, 10)]
    for row in grid:
        if sorted(row) != match:
            return False
    for column_index in range(9):
        column = [grid[row_index][column_index] for row_index in range(9)]
        if sorted(column) != match:
            return False
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            box = []
            box.extend(grid[row][column:column + 3])
            box.extend(grid[row + 1][column:column + 3])
            box.extend(grid[row + 2][column:column + 3])
            if sorted(box) != match:
                return False
    return True
