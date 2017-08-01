def isIPv4Address(inputString):
    strings = [string for string in inputString.split('.')]
    for string in strings:
        if not string.isdecimal():
            return False
    nums = [int(num) for num in strings]
    return max(nums) <= 255 and min(nums) >= 0 and len(nums) == 4
