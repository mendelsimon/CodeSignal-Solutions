def sumUpNumbers(inputString):
    total = 0
    current_num = []
    for char in inputString:
        if char.isdigit():
            current_num.append(char)
        else:
            if len(current_num) > 0:
                num = int("".join(current_num))
                total += num
                current_num = []
    if len(current_num) > 0:
        num = int("".join(current_num))
        total += num
    return total
