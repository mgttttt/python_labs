# run_cython.py
from my import calc
from time import time

if __name__ == '__main__':
    t = time()
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    print(calc(n, m))
    end = time() - t
    print(end, 'мс')
