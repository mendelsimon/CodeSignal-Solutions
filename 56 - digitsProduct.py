def digitsProduct(product):
    # New idea: add product to factors
    # while max(factors) > 10: split that num into factors
    if product == 0:
        return 10

    factors = [product]
    while max(factors) > 9:
        factored = findFactors(max(factors))
        if factored:
            factors.remove(max(factors))
            factors.extend(factored)
        else:
            return -1

    while factors.count(3) >= 2:
        factors.remove(3)
        factors.remove(3)
        factors.append(9)

    while factors.count(2) > 2:
        factors.remove(2)
        factors.remove(2)
        factors.remove(2)
        factors.append(8)

    while factors.count(2) > 1:
        factors.remove(2)
        factors.remove(2)
        factors.append(4)

    while 2 in factors and 3 in factors:
        factors.remove(2)
        factors.remove(3)
        factors.append(6)

    return int("".join(map(str, sorted(factors))))


def findFactors(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return False
