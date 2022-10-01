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
    matrixview = matrix[::-1]

    # imprimo la matriz para ver lo que devuelve
    return matrixview, alignment_cost, normalized_alignment_cost


print(dtw(lista1, lista2))

def movimiento(m, signo, i, j): # función para obtener el movimiento dentro de la matriz
    if signo == 0: # si el signo es 0, el movimiento es diagonal
        return m[i-1][j-1]
    elif signo == 1: # si el signo es 1, el movimiento es vertical hacia arriba
        return m[i-1][j]
    elif signo == 2: # si el signo es 2, el movimiento es horizontal hacia la izquierda
        return m[i][j-1]

# funcion para registrar el indice de los valores que luego saco en el camino
indice = []
def indices(m, i, j):
    indice.append([i, j])
    return indice

recorrido = []
def camino(m, i, j): # función para obtener el camino
    if i == 0 and j == 0: # si i y j son 0 paramos
        recorrido.append(matrix[i][j])
        indices(m, i, j)
    else:
        # obtengo los valores de la matriz en la posición i,j
        diagonal, vertical, horizontal = m[i-1][j-1], m[i-1][j], m[i][j-1]
        # obtengo el valor mínimo de los 3
        minimo = min(diagonal, vertical, horizontal)
        # si el valor mínimo es el de la diagonal, el movimiento es diagonal
        if minimo == diagonal:
            recorrido.append(matrix[i][j])
            indices(m, i, j)
            camino(m, i-1, j-1)
        # si el valor mínimo es el de la vertical, el movimiento es vertical
        elif minimo == vertical:
            recorrido.append(matrix[i][j])
            indices(m, i, j)
            camino(m, i-1, j)
        # si el valor mínimo es el de la horizontal, el movimiento es horizontal
        elif minimo == horizontal:
            recorrido.append(matrix[i][j])
            indices(m, i, j)
            camino(m, i, j-1)
    return recorrido
print(camino(matrix, n, m))
print(indice)
listaplus5 = []

for i in range(len(lista1)): # este bucle es para que no se me solapen las lineas
    listaplus5.append(lista1[i]+(max(lista1+lista2)))

# dibuja la lista 1 
plt.plot(listaplus5, marker='o')
# dibuja la lista 2
plt.plot(lista2, marker='o')
# las muestra
plt.show()