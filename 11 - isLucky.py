def isLucky(n):
    string = str(n)
    top = [int(x) for x in string[:len(string)//2]]
    bottom = [int(x) for x in string[len(string)//2:]]
    return sum(top) == sum(bottom)