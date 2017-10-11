def candles(candlesNumber, makeNew):
    totalBurned = 0
    leftovers = 0
    while candlesNumber > 0:
        totalBurned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = 0
        candlesNumber = leftovers // makeNew
        leftovers = leftovers % makeNew
    return totalBurned
