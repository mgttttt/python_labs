from math import sqrt


def calc_len(coords):
    return sqrt((coords[0][0] - coords[1][0]) ** 2 + (coords[0][1] - coords[1][1]) ** 2)


def triangle_square(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    else:
        return 0


def calc_r(s, a, b, c):
    r = 0
    if s:
        p = (a + b + c) / 2
        r = s / p
    return r


def calc_R(s, a, b, c):
    R = 0
    if s:
        R = a * b * c / (4 * s)
    return R