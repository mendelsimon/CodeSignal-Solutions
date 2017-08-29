def fileNaming(names):
    outnames = []
    for name in names:
        if name in outnames:
            k = 1
            while "{}({})".format(name, k) in outnames:
                k += 1
            name = "{}({})".format(name, k)
        outnames.append(name)
    return outnames
