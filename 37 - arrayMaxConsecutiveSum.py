def arrayMaxConsecutiveSum(inputArray, k):
    sums = [sum(inputArray[:k])]
    for i in range(1, len(inputArray) - k + 1):
        sums.append(sums[i - 1] - inputArray[i - 1] + inputArray[i + k - 1])
    return max(sums)
