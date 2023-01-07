from cython.cimports.libc.math import sin, pow, sqrt

cdef double f(double x):
    return sin(pow(1.3, x) - 1.2)

cdef double g(double x):
    return sin(x) - 1.0 / (1 + x * x)

cpdef calc(int n, int m):
    cdef double res = 0.0
    for i in range(n):
        for j in range(m):
            res += pow(f(i + 1) + g(j + 1), 2)
    return round(sqrt(res), 6)

