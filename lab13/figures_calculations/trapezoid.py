from math import sqrt, fabs
from .triangle import triangle_square


def parallel(coords):
    k1 = (coords[0][0][1] - coords[0][1][1]) / (coords[0][0][0] - coords[0][1][0])
    k2 = (coords[1][0][1] - coords[1][1][1]) / (coords[1][0][0] - coords[1][1][0])
    return fabs(k1 - k2) <= 0.01


def calc(a, b, c, d, e):
    s1 = triangle_square(a, c, e)
    s2 = triangle_square(e, c, d)
    if not s1 or not s2:
        return 0
    else:
        return s1 + s2


def calc_r(a, b, c, d):
    if a + d == c + b:
        return sqrt(a * d) / 2
    return 0


def calc_R(a, b, c, d, e):
    s1 = triangle_square(a, c, e)
    s2 = triangle_square(e, c, d)
    R1 = a * e * c / (4 * s1)
    R2 = d * e * c / (4 * s2)
    if fabs(R1 - R2) <= 0.01:
        return R1
    else:
        return 0