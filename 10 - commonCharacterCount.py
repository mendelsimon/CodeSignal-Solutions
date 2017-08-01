def commonCharacterCount(s1, s2):
    count = 0
    word2 = list(s2)
    for letter in s1:
        if letter in word2:
            word2.remove(letter)
            count += 1
    return count
