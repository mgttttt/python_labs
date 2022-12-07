from math import sqrt, fabs

n = int(input('Enter n: '))
m = int(input('Enter m: '))

matrix = [[] for _ in range(n)]
f = lambda x: (5 * x * x - 8) / (x ** 3 + 1)
g = lambda x: (sqrt(x + 1) - sqrt(x) - 0.5)

res = -10e9

for i in range(n):
    for j in range(m):
        matrix[i].append(f(i) + g(j))
        if fabs(matrix[i][j]) > res:
            res = fabs(matrix[i][j])

print(round(res * sqrt(n * m), 6))