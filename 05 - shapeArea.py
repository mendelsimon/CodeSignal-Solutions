def shapeArea(n):
    sum = n*2 - 1
    for i in range(1, (n*2)-1, 2):
        sum += i*2
    return sum