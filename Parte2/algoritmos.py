import numpy as np

lista1 = [1,4,2,1]
lista2 = [3,1,1,3]

def dtw(a, b):
    
    n, m = len(a), len(b) # obtengo n y m que son las dimensiones de las listas introducidas
    matrix = np.zeros((n+1, m+1)) # creo matriz de ceros
    matrix[0, 1:], matrix[1:, 0] = np.inf, np.inf # establezco los infinitos
    matrix[1][2] = 1 # simples pruebas
    matrix = matrix[::-1] # dejo colocada como me interesa personalmente la matriz para poder verla bien
    
    print(matrix) # imprimo la matriz para ver lo que devuelve

dtw(lista1, lista2)