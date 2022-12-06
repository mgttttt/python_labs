from math import sqrt
from . import triangle2
from . import figure


class Rectangle(figure.Figure):
    coords = None
    a, b, c, d, e = 0, 0, 0, 0, 0
    s, r, R = 0, 0, 0

    def __init__(self, coords):
        self.coords = coords
        tr = triangle2.Triangle([coords[0], coords[1], coords[3]])
        tr2 = triangle2.Triangle([coords[0], coords[2], coords[3]])
        if tr.s and tr2.s:
            self.a = tr.a
            self.c = tr.c
            self.e = tr.b
            self.d = tr2.c
            self.b = tr2.a
            self.s = tr.s + tr2.s
            self.calc_r()
            self.calc_R()

    def calc_r(self):
        self.r = self.a / 2 if self.a == self.b == self.c else 0

    def calc_R(self):
        self.R = sqrt(self.a ** 2 + self.b ** 2) / 2