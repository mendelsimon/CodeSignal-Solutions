def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 30 or lastNumberOfDays == 28:
        return [31]
    return [28, 30, 31]
