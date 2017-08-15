def isBeautifulString(inputString):
    for letter in range(ord('a'), ord('z')):
        if inputString.count(chr(letter)) < inputString.count(chr(letter + 1)):
            return False
    return True
