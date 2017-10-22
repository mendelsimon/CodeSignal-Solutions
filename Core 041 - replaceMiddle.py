def replaceMiddle(arr):
    if len(arr) % 2 != 0:
        return arr
    right_middle = len(arr) // 2
    middle_value = arr[right_middle] + arr[right_middle - 1]
    return arr[:right_middle - 1] + [middle_value] + arr[right_middle + 1:]
