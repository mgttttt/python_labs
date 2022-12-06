from . import triangle2
from math import sqrt, fabs
from . import figure


class Trapezoid(figure.Figure):
    a, b, c, d, e = 0, 0, 0, 0, 0
    s, r, R = 0, 0, 0
    coords = None

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
            self.calc_R(tr, tr2)

    def calc_r(self):
        self.r = sqrt(self.a * self.d) / 2 if self.a + self.d == self.c + self.b else 0

    def calc_R(self, tr1, tr2):
        s1 = tr1.s
        s2 = tr2.s
        if s1:
            R1 = self.a * self.e * self.c / (4 * s1)
        if s2:
            R2 = self.d * self.e * self.c / (4 * s2)
        self.R = R1 if fabs(R1 - R2) <= 0.01 else 0

