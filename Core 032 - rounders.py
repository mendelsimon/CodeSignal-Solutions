def rounders(value):
    length = len(str(value))
    magnitude = length - 1
    for i in range(length - 1):
        value = int((value / 10) + 0.5)
    return value * (10 ** magnitude)
