def pagesNumberingWithInk(current, numberOfDigits):
    numberOfDigits -= len(str(current))
    next_digits = len(str(current + 1))
    while numberOfDigits >= next_digits:
        current += 1
        numberOfDigits -= next_digits
        next_digits = len(str(current))
    return current
