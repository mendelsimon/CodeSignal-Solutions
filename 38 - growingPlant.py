def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 1
    height += upSpeed
    while height < desiredHeight:
        days += 1
        height -= downSpeed
        height += upSpeed
    return days
