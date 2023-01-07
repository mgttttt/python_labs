# run_numba.py
from math import sin, sqrt
from numba import njit, prange
from time import time

@njit
def f(x):
    return sin(1.3 ** (x) - 1.2)

@njit
def g(x):
    return sin(x) - 1 / (1 + x ** 2)

@njit(parallel=True)
def calc(n, m):
    res = 0
    for i in prange(n):
        for j in prange(m):
            res += (f(i + 1) + g(j + 1)) ** 2
    return round(sqrt(res), 6)


if __name__ == '__main__':
    t = time()
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    print(calc(n, m))
    end = time() - t
    print(end, 'мс')
