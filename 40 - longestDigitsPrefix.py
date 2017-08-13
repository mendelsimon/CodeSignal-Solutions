def longestDigitsPrefix(inputString):
    for char in range(len(inputString)):
        if not inputString[char].isdigit():
            return inputString[:char]
    return inputString
