def maxMultiple(divisor, bound):
    for num in range(bound, 1, -1):
        if num % divisor == 0:
            return num
    return 0
