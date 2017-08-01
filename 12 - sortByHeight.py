def sortByHeight(a):
    treePositions = [x for x in range(len(a)) if a[x] == -1]
    people = sorted([x for x in a if x != -1])
    for tree in treePositions:
        people.insert(tree, -1)
    return people
