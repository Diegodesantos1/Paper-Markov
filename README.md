<h1 align="center">Tarea Inicial</h1>

<h3 align="center">Perfiles de GitHub de los autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
2. [@Diegodesantos1](https://github.com/Diegodesantos1)
3. [@mat0ta](https://github.com/mat0ta)
4. [@XaviTheForce](https://github.com/Xavitheforce)

---
En este [repositorio](https://github.com/Diegodesantos1/Paper-Markov) queda resuelto el ejercicio de la Tarea Inicial.
***

<h2 align="center">Parte 1: Ejercicio de Látex</h2>

Hemos traducido el pdf original y lo hemos pasado a LaTeX, utilizando Overleaf y Replit para hacer el trabajo colaborativo.

<h2 align="center"> Parte 2: Programar DTW</h2>

Para programar este algoritmo, primero nos hemos tenido que documentar a través de diferentes medios para luego poder programarlo de la forma más óptima y sobre todo original.

Hemos creado el código en base a listas de números lo cual sería fácilmente extrapolable a los datos de por ejemplo 2 datasets y tratar de ver la relación que haya o no entre ellos. Posteriormente no solo hemos obtenido la matriz de coste sino que también el llamado coste, también lo hemos normalizado y una vez obtuvimos todos esos datos conseguimos encontrar el camino más óptimo el cual también lo representamos visualmente empleando la librería de matplotlib.

El código es el siguiente:

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd
import random


def seleccion():
    global lista1, lista2
    eleccion = int(input("""Elija una opción: 1: listas aleatorias, 2: csv temperaturas
    """))

    if eleccion == 1:
        len = int(input("Introduzca la longitud de las listas: "))
        lista1, lista2 = [random.randint(0, 25) for x in range(len)], [
            random.randint(0, 25) for x in range(len)]
        print(lista1, lista2)
        return lista1, lista2
    elif eleccion == 2:
        datos = pnd.read_csv(
            "Parte2/spanish_daily_mean_n.csv", header=0, sep=",")
        datos2 = pnd.read_csv("Parte2/us_daily_mean_n.csv", header=0, sep=",")
        datos = datos.to_numpy()
        datos2 = datos2.to_numpy()
        lista1 = datos[:, 1]
        lista2 = datos2[:, 1]
        return lista1, lista2
    else:
        print("Opción incorrecta")
        seleccion()


seleccion()


def dtw(a, b):
    global matrix, n, m
    n, m = len(a), len(b)
    matrix = np.zeros((n+1, m+1))  # creo matriz de ceros
    matrix[0, 1:], matrix[1:, 0] = np.inf, np.inf  # establezco los infinitos

    for i in range(1, n+1):  # recorro filas
        for j in range(1, m+1):  # recorro columnas
            # obtengo una lista con los valores minimos que me interesan
            list_values = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]
            # calculo la distancia entre a(i) y b(j) y le sumo el valor minimo de la lista
            matrix[i][j] = abs(a[i-1]-b[j-1]) + min(list_values)
    alignment_cost, normalized_alignment_cost, matrixview = matrix[len(
        a)][len(b)], matrix[len(a)][len(b)]/(n+m), matrix[::-1]
    return matrixview, alignment_cost, normalized_alignment_cost


print(dtw(lista1, lista2))

indice, recorrido = [], []
lista1plus = []
for x in range(0, len(lista1)):
    lista1plus.append(lista1[x]+max(lista1+lista2)*2)


def camino(m, i, j):  # función para obtener el camino
    if i == 0 and j == 0:  # si i y j son 0 paramos
        return recorrido
    else:
        diagonal, vertical, horizontal = m[i-1][j-1], m[i-1][j], m[i][j-1]
        minimo = min(diagonal, vertical, horizontal)
        if minimo == diagonal:
            recorrido.append(matrix[i][j]), indice.append(
                [i, j]), camino(m, i-1, j-1)
        elif minimo == vertical:
            recorrido.append(matrix[i][j]), indice.append(
                [i, j]), camino(m, i-1, j)
        elif minimo == horizontal:
            recorrido.append(matrix[i][j]), indice.append(
                [i, j]), camino(m, i, j-1)


camino(matrix, n, m), print(indice)
plt.plot(lista1plus, marker='o')
plt.plot(lista2, marker='o')

for i in range(len(indice)):  # dibuja las lineas
    for j in range(len(lista1plus)):
        if indice[i][0] == j+1:
            plt.plot([j, indice[i][1]-1], [lista1plus[j],
                     lista2[indice[i][1]-1]], color='red', linewidth=0.5)
plt.savefig("Parte2/imagen_grafico/dtw.png")
plt.show()
```

Una muestra de su ejecución podría ser esta en la cual se basa en las listas [21, 21, 16, 0, 9, 9, 17, 3, 0, 4] y [21, 7, 25, 11, 1, 12, 10, 10, 5, 10] y obtenemos lo siguiente:

<p align="center">
  <img src="https://github.com/Diegodesantos1/Paper-Markov/blob/c823400ed78be31f7aabc48723b9a77ab815fed0/Parte2/imagen_grafico/dtw.png"/>
</p>

<h2 align="center"> Parte 3: Programar Markov</h2>

Primero, para poder comenzar a trabajar hemos seleccionado un dataset y hemos realizado su analisis básico inicial para tener datos sobre los que trabajar.

En esta parte del trabajo hemos programado un algoritmo que hace uso de las cadenas ocultas de Markov para calcular la probabilidad de que ocurran determinadas secuencias de estados (en este caso v= defectuoso y nv= no defectuoso) dependiendo de otros factores externos (en este caso 3 fabricas distintas Sol, Lluv y Niev de las que salen los productos).
En esencia, defines una cadena de estos estados y, basándose en probabilidades ya definidas de antemano,(gracias a nuestro maravilloso dataset) el codigo va calculando aplicando la matriz de Markov y las "frecuencias" de los estados las probabilidades de que los productos salgan de esa manera de una fábrica u otra. Al final, se suma la última lista creada con los resultados finales para dar con la probabilidad final y real de esa cadena de estados teniendo en cuenta las 3 fábricas iniciales.

<h2 align="center"> Parte 4: Conclusiones</h2>

Las cadenas ocultas de Markov junto con el uso del Dynamic Time Warping tienen una infinidad de usos, entre ellos la de predecir, basandose en hechos pasados, acciones futuras en función de parámetros que relacionan estos ultimos con variables que se pueden medir y calcular matemátimamente. También predicen secuencias de acciones u estados, como visto en el ejemplo algorítmico planteado y pueden incluso (como visto en el documento sobre el que hemos trabajado) ayudar a integrar procesos computacionales de manera rápida y eficaz en la industria moderna.
