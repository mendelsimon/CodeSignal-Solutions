import itertools

def stringsRearrangement(inputArray):
    permutations = itertools.permutations(inputArray)
    for array in permutations:
        if testArrangement(array):
            return True
    return False

def testArrangement(array):
    for i in range(len(array) - 1):
        if sum([a != b for a, b in zip(array[i], array[i + 1])]) != 1:
            return False
    return True
