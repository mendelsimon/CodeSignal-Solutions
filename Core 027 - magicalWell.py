def magicalWell(a, b, n):
    total = 0
    for i in range(n):
        total += a * b
        a += 1
        b += 1
    return total
