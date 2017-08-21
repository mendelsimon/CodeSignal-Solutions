def lineEncoding(s):
    count = 1
    output = []
    for char in range(1, len(s)):
        if s[char] == s[char - 1]:
            count += 1
        else:
            if count > 1:
                output.append(str(count) + s[char - 1])
            else:
                output.append(s[char - 1])
            count = 1
    if s[len(s) - 1] == s[len(s) - 2]:
        output.append(str(count) + s[len(s) - 1])
    else:
        output.append(s[len(s) - 1])
    return ''.join(output)
