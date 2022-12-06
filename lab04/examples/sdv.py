def is_pallindrom(n):
    n_copy, reverse_n = n, 0
    while n_copy:
        reverse_n = reverse_n * 10 + n_copy % 10
        n_copy //= 10
    return reverse_n == n


for i in range(11, 100, 11):
    if is_pallindrom(i ** 3):
        print(i)
