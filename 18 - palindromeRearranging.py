def palindromeRearranging(inputString):
    inputList = sorted(inputString)
    foundMiddle = False
    while len(inputList) > 1:
        if inputList[0] == inputList[1]:
            del inputList[1]
        elif not foundMiddle:
            foundMiddle = True
        else:
            return False
        del inputList[0]
    return len(inputList) == 0 or not foundMiddle
