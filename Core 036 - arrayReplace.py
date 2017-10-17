def arrayReplace(inputArray, elemToReplace, substitutionElem):
    output = [elem if elem != elemToReplace else substitutionElem for elem in inputArray]
    return output