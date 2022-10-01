import numpy as np
import matplotlib.pyplot as plt

lista1 = [1, 4, 2, 1]
lista2 = [3, 1, 1, 3]

def dtw(a, b):
    global matrix, n, m
    # obtengo n (filas) y m (columnas) que son las dimensiones de las listas introducidas
    n, m = len(a), len(b)
    matrix = np.zeros((n+1, m+1))  # creo matriz de ceros
    matrix[0, 1:], matrix[1:, 0] = np.inf, np.inf  # establezco los infinitos

    """Para generar mi matriz y obtener los elementos me he basado en la explicación del algoritmo del siguiente video:
    https://www.youtube.com/watch?v=9GdbMc4CEhE
    """

    for i in range(1, n+1):  # recorro filas
        for j in range(1, m+1):  # recorro columnas
            # obtengo una lista con los valores minimos que me interesan
            list_values = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]
            # calculo la distancia entre a(i) y b(j) y le sumo el valor minimo de la lista
            matrix[i][j] = abs(a[i-1]-b[j-1]) + min(list_values)

    alignment_cost = matrix[len(a)][len(b)]  # añado el alignment cost
    # lo normalizo dividiendo entre la suma de las longitudes de las listas
    normalized_alignment_cost = alignment_cost/(n+m)
    # dejo colocada como me interesa personalmente la matriz para poder verla bien

    # imprimo la matriz para ver lo que devuelve
    return matrix, alignment_cost, normalized_alignment_cost


print(dtw(lista1, lista2))

def movimiento(m, signo, i, j): # función para obtener el movimiento dentro de la matriz
    if signo == 1: # si el signo es 1, el movimiento es diagonal
        return m[i-1][j-1]
    elif signo == 2: # si el signo es 2, el movimiento es vertical hacia arriba
        return m[i-1][j]
    elif signo == 3: # si el signo es 3, el movimiento es horizontal hacia la izquierda
        return m[i][j-1]
for i in range(n+1,0,-1): # recorro la matriz de abajo hacia arriba
    for j in range(m+1,0,-1): # recorro la matriz de derecha a izquierda
        # obtengo una lista con los valores minimos que me interesan
        lista_valores = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]] # el primer elemento de la lista es el diagonal, 
        #el segundo el vertical y el tercero el horizontal
        
"""
listaplus5 = []

for i in range(len(lista1)): # este bucle es para que no se me solapen las lineas
    listaplus5.append(lista1[i]+(max(lista1+lista2)))

Ahora usando matplotlib muestro las listas en un grafico
# dibuja la lista 1 
plt.plot(listaplus5, marker='o')
# dibuja la lista 2
plt.plot(lista2, marker='o')
# las muestra
plt.show()"""