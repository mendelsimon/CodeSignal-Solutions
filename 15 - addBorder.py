def addBorder(picture):
    picture = ["*" + string + "*" for string in picture]
    picture = [("*" * len(picture[0]))] + picture + [("*" * len(picture[0]))]
    return picture
