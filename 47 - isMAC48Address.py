def isMAC48Address(inputString):
    hex_chars = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 'A', 'B', 'C', 'D', 'E', 'F',
                 'a', 'b', 'c', 'd', 'e', 'f')
    groups = inputString.split('-')
    if len(groups) != 6:
        return False
    if not all((len(group) == 2 for group in groups)):
        return False
    if not all((group[0] in hex_chars and group[1] in hex_chars for group in groups)):
        return False
    return True
