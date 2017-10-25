def isSumOfConsecutive2(n):
    count = 0
    right = 2
    arr = [1, 2]
    while right <= (n // 2) + 1:
        total = sum(arr)
        if total == n:
            count += 1
            del arr[0]
        elif total < n:
            right += 1
            arr.append(right)
        elif total > n:
            del arr[0]
    return count
