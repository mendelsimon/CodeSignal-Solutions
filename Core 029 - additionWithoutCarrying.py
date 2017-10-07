def additionWithoutCarrying(param1, param2):
    # Convert numbers to strings
    str1 = str(param1)
    str2 = str(param2)
    # Pad both to the same length with zeroes (to the left of the numbers)
    length = max(len(str2), len(str1))
    str1 = str1.rjust(length, '0')
    str2 = str2.rjust(length, '0')
    output = []
    for num1, num2 in zip(str1, str2):
        result = str(int(num1) + int(num2))[-1]
        output.append(result)
    return int(''.join(output))
