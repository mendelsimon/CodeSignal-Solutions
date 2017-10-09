def increaseNumberRoundness(n):
    string = str(n)
    # Check for immediate rejection
    if '0' not in string or len(string) < 2:
        return False
    # Since we know there's a 0, if it's not on
    # the left, then we know to accept
    if string[-1] != '0':
        return True
    # If there is only one 0, it must be at the end, so reject.
    if string.count('0') == 1:
        return False
    # If there are any numbers between the first 0
    # and the end of the string, then accept.
    first_zero = string.find('0')
    zero_sandwich = string[first_zero:]
    return zero_sandwich.count('0') != len(zero_sandwich)
