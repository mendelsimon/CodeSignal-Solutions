def bishopAndPawn(bishop, pawn):
    return abs(ord(bishop[0]) - ord(pawn[0])) == abs(ord(bishop[1]) - ord(pawn[1]))
