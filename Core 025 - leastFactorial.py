def leastFactorial(n):
    factorial = 1
    index = 1
    while factorial < n:
        index += 1
        factorial *= index
    return factorial
