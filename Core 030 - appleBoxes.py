def appleBoxes(k):
    red = 0
    yellow = 0
    for i in range(1, k + 1, 2):
        yellow += i * i
    for i in range(2, k + 1, 2):
        red += i * i

    return red - yellow
