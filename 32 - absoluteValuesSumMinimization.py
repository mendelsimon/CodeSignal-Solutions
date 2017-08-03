def absoluteValuesSumMinimization(a):
    sums = {}
    for num in a:
        total = sum([abs(a[i] - num) for i in range(len(a))])
        if total in sums:
            sums[total] = min(num, sums[total])
        else:
            sums[total] = num
        print(sums)
    return sums[min(sums)]
