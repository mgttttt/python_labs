# run_numba.py
from math import sin, sqrt
from numba import njit, prange, int32, double
from time import time

@njit(double(double))
def f(x):
    return sin(1.3 ** (x) - 1.2)

@njit(double(double))
def g(x):
    return sin(x) - 1 / (1 + x ** 2)

@njit(double(int32, int32))
def calc(n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            res += (f(i + 1) + g(j + 1)) ** 2
    return round(sqrt(res), 6)


if __name__ == '__main__':
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    t = time()
    print(calc(n, m))
    end = time() - t
    print(end * 100, 'мс')
