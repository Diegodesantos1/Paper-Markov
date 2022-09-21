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

<h2 align="center"> Parte 2: Programar Markov</h2>

Primero, para poder comenzar a trabajar hemos seleccionado un dataset y hemos realizado su analisis básico inicial para tener datos sobre los que trabajar.

En esta parte del trabajo hemos programado un algoritmo que hace uso de las cadenas ocultas de Markov para calcular la probabilidad de que ocurran determinadas secuencias de estados (en este caso v= defectuoso y nv= no defectuoso) dependiendo de otros factores externos (en este caso 3 fabricas distintas Sol, Lluv y Niev de las que salen los productos).
En esencia, defines una cadena de estos estados y, basándose en probabilidades ya definidas de antemano,(gracias a nuestro maravilloso dataset) el codigo va calculando aplicando la matriz de Markov y las "frecuencias" de los estados las probabilidades de que los productos salgan de esa manera de una fábrica u otra. Al final, se suma la última lista creada con los resultados finales para dar con la probabilidad final y real de esa cadena de estados teniendo en cuenta las 3 fábricas iniciales.

<h2 align="center"> Parte 3: Conclusiones</h2>

Las cadenas ocultas de Markov junto con el uso del Dynamic Time Warping tienen 