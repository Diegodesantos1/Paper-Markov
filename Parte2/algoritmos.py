import numpy as np

lista1 = [1,4,2,1]
lista2 = [3,1,1,3]

def dtw(a, b):
    n, m = len(a), len(b)
    matrix = np.zeros((n+1, m+1))
    matrix[0, 1:], matrix[1:, 0] = np.inf, np.inf

    print(matrix)

dtw(lista1, lista2)