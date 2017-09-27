def swapAdjacentBits(n):
    return ((n >> 1) & 1431655765) | ((n << 1) & 2863311530)
