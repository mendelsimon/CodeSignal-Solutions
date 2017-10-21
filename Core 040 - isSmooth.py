def isSmooth(arr):
    if arr[0] != arr[-1]:
        return False
    if len(arr) % 2 == 0:
        middle = arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]
    else:
        middle = arr[len(arr) // 2]
    return arr[0] == middle