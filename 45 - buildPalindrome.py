def buildPalindrome(st):
    if st == st[::-1]:  # Check for initial palindrome
        return st
    index = 0
    subStr = st[index:]
    while subStr != subStr[::-1]:  # while substring is not a palindrome
        index += 1
        subStr = st[index:]
    return st + st[index - 1::-1]
