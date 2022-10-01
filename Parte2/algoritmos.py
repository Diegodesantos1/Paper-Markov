import numpy as np

lista1 = [1,4,2,1]
lista2 = [3,1,1,3]

def dtw(a, b):
    n, m = len(a), len(b)
    matrix = np.zeros((n+1, m+1))
    print(matrix)

dtw(lista1, lista2)