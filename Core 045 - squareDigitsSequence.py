def squareDigitsSequence(a0):
    sequence = [a0]
    while sequence[-1] not in sequence[:-1]:
        next_value = 0
        for digit in str(sequence[-1]):
            next_value += int(digit) ** 2
        sequence.append(next_value)
    return len(sequence)
