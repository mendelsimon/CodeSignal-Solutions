def evenDigitsOnly(n):
    return all((True if digit in ('0', '2', '4', '6', '8') else False for digit in str(n)))
