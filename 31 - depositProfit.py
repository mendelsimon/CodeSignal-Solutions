def depositProfit(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        deposit *= 1 + (rate / 100)
        year += 1
    return year
