import numpy as np
import matplotlib.pyplot as plt

lista1, lista2 = [1,4,2,1,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12]

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

    alignment_cost, normalized_alignment_cost, matrixview = matrix[len(a)][len(b)], matrix[len(a)][len(b)]/(n+m), matrix[::-1] 
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
    indice.append([i, j]), indice.sort()
    return indice

recorrido = []
def camino(m, i, j): # función para obtener el camino
    if i == 0 and j == 0: # si i y j son 0 paramos
        return recorrido
    else:
        # obtengo los valores de la matriz en la posición i,j
        diagonal, vertical, horizontal = m[i-1][j-1], m[i-1][j], m[i][j-1]
        # obtengo el valor mínimo de los 3
        minimo = min(diagonal, vertical, horizontal)
        # si el valor mínimo es el de la diagonal, el movimiento es diagonal
        if minimo == diagonal:
            recorrido.append(matrix[i][j]), indices(m, i, j), camino(m, i-1, j-1)
        # si el valor mínimo es el de la vertical, el movimiento es vertical
        elif minimo == vertical:
            recorrido.append(matrix[i][j]), indices(m, i, j), camino(m, i-1, j)
        # si el valor mínimo es el de la horizontal, el movimiento es horizontal
        elif minimo == horizontal:
            recorrido.append(matrix[i][j]),indices(m, i, j),camino(m, i, j-1)

camino(matrix, n, m),print(indice)

# siendo dentro de la lista indice en cada sublista el primer valor el indice de la lista1 y el segundo el de la lista2
# creo una funcion que me diga que valores de la lista1 y lista2 son los que se han alineado
def alineados(indice):
    global lista_alineados 
    lista_alineados = []
    for i in indice:
        lista_alineados.append([lista1[i[0]-1], lista2[i[1]-1]])
    return lista_alineados

alineados(indice)
lista1plus = []
for i in range(len(lista1)):
    lista1plus.append(lista1[i]+5)
# dibuja las series
plt.plot(lista1plus, marker='o'),plt.plot(lista2, marker='o')

for i in range(len(indice)): # dibuja las lineas
    for j in range(len(lista1)):
        if indice[i][0] == j+1:
            plt.plot([j, indice[i][1]-1], [lista1plus[j], lista2[indice[i][1]-1]], color='red')
        
plt.show()