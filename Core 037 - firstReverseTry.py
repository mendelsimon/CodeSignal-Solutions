def firstReverseTry(arr):
    if len(arr) < 2:
        return arr
    if len(arr) < 4:
        return arr[::-1]
    return arr[-1:] + arr[1:-1] + arr[:1]
