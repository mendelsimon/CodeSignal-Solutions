def extractEachKth(inputArray, k):
    return [inputArray[x] for x in range(len(inputArray)) if (x + 1) % k != 0]
