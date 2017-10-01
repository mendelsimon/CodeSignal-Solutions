def countSumOfTwoRepresentations2(n, l, r):
    count = 0
    a = max(n - r, l)
    b = n - a
    while a <= r and a <= b:
        count += 1
        a += 1
        b -= 1
    return count
