def countBlackCells(n, m):
    gcd = find_gcd(n, m)
    line_cells = n + m - gcd
    line_corner_cells = (gcd - 1) * 2
    return line_cells + line_corner_cells


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
