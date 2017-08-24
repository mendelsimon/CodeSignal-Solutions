def longestWord(text):
    longest = []
    word = []
    for char in text:
        if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z"):
            word.append(char)
        else:
            if len(word) > len(longest):
                longest = word
            word = []
    if len(word) > len(longest):
        longest = word
    return "".join(longest)