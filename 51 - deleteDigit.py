def deleteDigit(n):
    num = str(n)
    highest = 0
    for digit in range(len(num)):
        output = num[:digit] + num[digit + 1:]
        if int(output) > int(highest):
            highest = output
    return int(highest)
