def comfortableNumbers(l, r):
    count = 0
    for a in range(l, r):
        for b in range(a + 1, r + 1):
            a_sum = sum(int(digit) for digit in str(a))
            b_sum = sum(int(digit) for digit in str(b))
            if b <= a + a_sum and a >= b - b_sum:
                count += 1
    return count
