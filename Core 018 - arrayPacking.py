def arrayPacking(a):
    binary_array = [bin(num)[2:].rjust(8, '0') for num in a]
    out_string = ''.join(binary_array[::-1])
    return int(out_string, 2)
