def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > max:
            max = inputArray[i] * inputArray[i+1]
    return max
