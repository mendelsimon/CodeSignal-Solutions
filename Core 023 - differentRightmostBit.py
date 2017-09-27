def differentRightmostBit(n, m):
    return 2 ** bin((n ^ m))[::-1].find('1')
