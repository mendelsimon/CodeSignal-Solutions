def spiralNumbers(n):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    direction = RIGHT
    spiral = [[0 for i in range(n)] for j in range(n)]
    row = 0
    cell = 0
    for num in range(1, (n * n) + 1):
        spiral[row][cell] = num
        if direction == RIGHT:
            if cell != n - 1 and spiral[row][cell + 1] == 0:
                cell += 1
            else:
                direction = DOWN
                row += 1
        elif direction == DOWN:
            if row != n - 1 and spiral[row + 1][cell] == 0:
                row += 1
            else:
                direction = LEFT
                cell -= 1
        elif direction == LEFT:
            if cell != 0 and spiral[row][cell - 1] == 0:
                cell -= 1
            else:
                direction = UP
                row -= 1
        elif direction == UP:
            if row != 0 and spiral[row - 1][cell] == 0:
                row -= 1
            else:
                direction = RIGHT
                cell += 1
    return spiral


print(spiralNumbers(5))
