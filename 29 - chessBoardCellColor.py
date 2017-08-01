def chessBoardCellColor(cell1, cell2):
    color1 = ((ord(cell1[0]) - ord('A')) + ord(cell1[1]) - ord('1')) % 2 == 0
    color2 = ((ord(cell2[0]) - ord('A')) + ord(cell2[1]) - ord('1')) % 2 == 0
    return color1 == color2
