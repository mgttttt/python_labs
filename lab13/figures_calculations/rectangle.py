from math import sqrt
from .triangle import triangle_square


def calc(a, b, c, d, e):
    s1 = triangle_square(a, c, e)
    s2 = triangle_square(e, c, d)
    if not s1 or not s2:
        return 0
    else:
        return s1 + s2
    return s


def calc_r(a, b, c):
    return a / 2 if a == b == c else 0


def calc_R(a, b):
    return sqrt(a ** 2 + b ** 2) / 2

