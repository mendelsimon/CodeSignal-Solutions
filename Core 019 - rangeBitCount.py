def rangeBitCount(a, b):
    array = list(range(a, b + 1))
    binary_array = [bin(num) for num in array]
    count_array = [binary.count('1') for binary in binary_array]
    return sum(count_array)
