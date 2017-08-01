def allLongestStrings(inputArray):
    length = max([len(word) for word in inputArray])
    result = [word for word in inputArray if len(word) == length]
    return result