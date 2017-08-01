import re
def reverseParentheses(s):
    while "(" in s:
        match = re.search("\([^()]*\)", s)
        match_string = match.group(0)[1: len(match.group(0)) - 1]
        reversed_match_string = match_string[::-1]
        s = s[:match.start()] + reversed_match_string + s[match.end():]
    return s
