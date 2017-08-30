def messageFromBinaryCode(code):
    output = []
    for i in range(0, len(code), 8):
        letter = chr(int(code[i:i + 8], 2))
        output.append(letter)
    return ''.join(output)
