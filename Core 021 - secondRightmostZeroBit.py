def secondRightmostZeroBit(n):
    return 2 ** bin(n)[::-1].find('0', bin(n)[::-1].find('0') + 1)
