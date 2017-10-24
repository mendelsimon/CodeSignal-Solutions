def isPower(n):
    if n == 1:
        return True

    a = 2
    b = 2
    while a ** 2 <= n:
        while a ** b <= n:
            if a ** b == n:
                return True
            b += 1
        b = 2
        a += 1
    return False