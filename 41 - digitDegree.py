def digitDegree(n):
    degree = 0
    while len(str(n)) > 1:
        n = sum((int(digit) for digit in str(n)))
        degree += 1
    return degree
