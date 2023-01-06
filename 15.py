from math import sqrt, fabs, sin
from time import time

t = time()
n = int(input('Enter n: '))
m = int(input('Enter m: '))

matrix = [[] for _ in range(n)]
f = lambda x: sin(1.3 ** (x) - 1.2)
g = lambda x: sin(x) - 1 / (1 + x ** 2)

res = 0

for i in range(n):
    for j in range(m):
        matrix[i].append(f(i + 1) + g(j + 1))
        res += matrix[i][j] ** 2

print(round(sqrt(res), 6))
end = time() - t
print(end, 'мс')
