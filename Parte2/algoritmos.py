import numpy as np
import matplotlib.pyplot as plt

lista1, lista2 = [2, 0, 3, 8, 7, 2], [1, 3, 9, 3, 1]

def dtw(a, b):
    global matrix, n, m
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
    return matrixview, alignment_cost, normalized_alignment_cost

print(dtw(lista1, lista2))

# funcion para registrar el indice de los valores que luego saco en el camino
indice,recorrido = [], []

def camino(m, i, j): # función para obtener el camino
    if i == 0 and j == 0: # si i y j son 0 paramos
        return recorrido
    else:
        diagonal, vertical, horizontal = m[i-1][j-1], m[i-1][j], m[i][j-1]
        minimo = min(diagonal, vertical, horizontal)
        if minimo == diagonal: recorrido.append(matrix[i][j]), indice.append([i, j]), camino(m, i-1, j-1)
        elif minimo == vertical: recorrido.append(matrix[i][j]), indice.append([i, j]), camino(m, i-1, j)
        elif minimo == horizontal: recorrido.append(matrix[i][j]),indice.append([i, j]),camino(m, i, j-1)

camino(matrix, n, m),print(indice)

lista1plus = [x + max(lista2) for x in lista1]
plt.plot(lista1plus, marker='o'),plt.plot(lista2, marker='o')
for i in range(len(indice)): # dibuja las lineas
    for j in range(len(lista1)):
        if indice[i][0] == j+1: plt.plot([j, indice[i][1]-1], [lista1plus[j], lista2[indice[i][1]-1]], color='red')
        
plt.show()