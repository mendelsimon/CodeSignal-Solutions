def boxBlur(image):
    outImage = []
    for row in range(1, len(image) - 1):
        line = []
        for pixel in range(1, len(image[row]) - 1):
            total = (image[row - 1][pixel - 1]
                     + image[row - 1][pixel]
                     + image[row - 1][pixel + 1]
                     + image[row][pixel - 1]
                     + image[row][pixel]
                     + image[row][pixel + 1]
                     + image[row + 1][pixel - 1]
                     + image[row + 1][pixel]
                     + image[row + 1][pixel + 1])
            line.append(total // 9)
        outImage.append(line)
    return outImage
