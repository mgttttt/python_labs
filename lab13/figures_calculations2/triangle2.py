from math import sqrt
from . import figure


class Triangle(figure.Figure):
    a, b, c = 0, 0, 0
    s, r, R = 0, 0, 0
    coords = None

    def __init__(self, coords):
        self.coords = coords
        self.a = self.calc_len([coords[0], coords[1]])
        self.b = self.calc_len([coords[0], coords[2]])
        self.c = self.calc_len([coords[2], coords[1]])
        self.triangle_square()
        if self.s:
            self.calc_r()
            self.calc_R()

    def calc_len(self, coords):
        return sqrt((coords[0][0] - coords[1][0]) ** 2 + (coords[0][1] - coords[1][1]) ** 2)

    def triangle_square(self):
        a, b, c = self.a, self.b, self.c
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            self.s = sqrt(p * (p - a) * (p - b) * (p - c))

    def calc_r(self):
        p = (self.a + self.b + self.c) / 2
        self.r = self.s / p

    def calc_R(self):
        self.R = self.a * self.b * self.c / (4 * self.s)