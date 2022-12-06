def is_pallindrom(n):
    str_n = str(n)
    len_n = len(str_n)
    for i in range(0, len_n // 2):
        if str_n[i] != str_n[len_n - i - 1]:
            return False
    return True


for i in range(11, 100, 11):
    if is_pallindrom(i ** 3):
        print(i)