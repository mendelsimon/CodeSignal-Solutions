def chessKnight(cell):
    moves = 0
    # Starting at the top left, going counter-clockwise
    if ord(cell[0]) >= ord("b") and ord(cell[1]) <= ord("6"):
        moves += 1
    if ord(cell[0]) >= ord("c") and ord(cell[1]) <= ord("7"):
        moves += 1
    if ord(cell[0]) >= ord("c") and ord(cell[1]) >= ord("2"):
        moves += 1
    if ord(cell[0]) >= ord("b") and ord(cell[1]) >= ord("3"):
        moves += 1
    if ord(cell[0]) <= ord("g") and ord(cell[1]) >= ord("3"):
        moves += 1
    if ord(cell[0]) <= ord("f") and ord(cell[1]) >= ord("2"):
        moves += 1
    if ord(cell[0]) <= ord("f") and ord(cell[1]) <= ord("7"):
        moves += 1
    if ord(cell[0]) <= ord("g") and ord(cell[1]) <= ord("6"):
        moves += 1

    return moves
