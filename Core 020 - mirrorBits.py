def mirrorBits(a):
    binary = bin(a)[2:]
    return int(binary[::-1], 2)
