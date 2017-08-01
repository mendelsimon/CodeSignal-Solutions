def areSimilar(a, b):
    diff = [i for i in range(len(a)) if a[i] != b[i]]
    if len(diff) == 2:
        b[diff[0]], b[diff[1]] = b[diff[1]], b[diff[0]]
    return a == b
