import numpy as np

lista1 = [1,4,2,1]
lista2 = [3,1,1,3]

def dtw(a, b):
    
    n, m = len(a), len(b) # obtengo n (filas) y m (columnas) que son las dimensiones de las listas introducidas
    matrix = np.zeros((n+1, m+1)) # creo matriz de ceros
    matrix[0, 1:], matrix[1:, 0] = np.inf, np.inf # establezco los infinitos
    
    """Para generar mi matriz y obtener los elementos me he basado en la explicación del algoritmo del siguiente video:
    https://www.youtube.com/watch?v=9GdbMc4CEhE
    """

    for i in range(1,n+1): # recorro filas
        for j in range(1,m+1): # recorro columnas
            list_values = [matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1]] # obtengo una lista con los valores minimos que me interesan
            matrix[i][j] = abs(a[i-1]-b[j-1]) + min(list_values) # calculo la distancia entre a(i) y b(j) y le sumo el valor minimo de la lista
    
    matrix = matrix[::-1] # dejo colocada como me interesa personalmente la matriz para poder verla bien

    print(matrix), print("matriz nxm") # imprimo la matriz para ver lo que devuelve

dtw(lista1, lista2)