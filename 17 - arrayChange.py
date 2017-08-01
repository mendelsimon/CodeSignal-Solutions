def arrayChange(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            difference = inputArray[i-1] - inputArray[i]
            inputArray[i] += difference + 1
            count += difference + 1
    return count
