def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [x if x != elemToReplace else substitutionElem for x in inputArray]
