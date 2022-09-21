import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def leerArchivo(csv):
        df = pd.read_csv(csv)
        return df

class Markov: #clase que calcula la probabilidad de que ocurra una secuencia determinada por probabilidades condicionadas
    tiempos = leerArchivo('Parte2/seattle-weather.csv')['weather'].tolist()
    del(tiempos[0])
    tiempo = []
    for causa in tiempos:
        if causa not in tiempo:
            tiempo.append(causa)
    print(tiempo)

    conteo=Counter(tiempos)

    dic_prob_tiempo={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor != 1:
            dic_prob_tiempo[clave] = valor
    print(dic_prob_tiempo)
    total = len(tiempos)
    prob_sol = dic_prob_tiempo['sun']/total
    prob_llu = dic_prob_tiempo['rain']/total
    prob_niev = dic_prob_tiempo['snow']/total
    #matriz probailiades condicionadas
    m_t = [[0.6, 0.2, 0.1], [0.5, 0.4, 0.1], [0.7, 0.2, 0.1]]
    #definimos las probabilidades relacionadas(definen el modelo de markov)
    v_s = 0.1
    nv_s = 0.9
    v_ll = 0.7
    nv_ll = 0.3
    v_n = 0.4
    nv_n = 0.6

    #para poder elegir el valor correspondiente en la formula markov
    def sacar_valor(letra):
        if letra == 'v':
            return [Markov.v_s, Markov.v_ll, Markov.v_n]
        else:
            return [Markov.nv_s, Markov.nv_ll, Markov.nv_n]

    #probabilidad de una secuencia de estados(los definidos aleatoria)
    def markov(secuencia):
        lista1 = []
        lista2 = []
        lista3 = []
        listadefi = []
        contador = 0
        for i in range(len(secuencia)):
            if contador == 0:
                a1 = Markov.sacar_valor(secuencia[contador])[0]*Markov.prob_sol
                a2 = Markov.sacar_valor(secuencia[contador])[1]*Markov.prob_llu
                a3 = Markov.sacar_valor(secuencia[contador])[2]*Markov.prob_niev
                lista1.append(a1)
                lista2.append(a2)
                lista3.append(a3)
            else:
                a1 = Markov.sacar_valor(secuencia[contador])[0]*(Markov.m_t[0][0]*lista1[contador-1]+Markov.m_t[1][0]*lista2[contador-1]+Markov.m_t[2][0]*lista3[contador-1])
                a2 = Markov.sacar_valor(secuencia[contador])[1]*(Markov.m_t[0][1]*lista1[contador-1]+Markov.m_t[1][1]*lista2[contador-1]+Markov.m_t[2][1]*lista3[contador-1])
                a3 = Markov.sacar_valor(secuencia[contador])[2]*(Markov.m_t[0][2]*lista1[contador-1]+Markov.m_t[1][2]*lista2[contador-1]+Markov.m_t[2][2]*lista3[contador-1])
                lista1.append(a1)
                lista2.append(a2)
                lista3.append(a3)
            contador+=1
        listadefi.append(lista1[-1])
        listadefi.append(lista2[-1])
        listadefi.append(lista3[-1])
        return listadefi

#Comprobamos con una secuencia cualquiera de nuestro markov si funciona
listadeprueba = ['v', 'nv', 'v', 'v', 'v', 'nv'] #Para probar si funciona markov
lista_probs = Markov.markov(['v', 'nv', 'v', 'v', 'v', 'nv'])
print("La probabilidad de que salga una secuencia del tipo "+str(listadeprueba)+" es de "+str((lista_probs[0]+lista_probs[1]+lista_probs[2])))

nsol = Markov.tiempos.count("sun")
nlluvia = Markov.tiempos.count("rain")
nnieve = Markov.tiempos.count("snow")

eje_x = ["Sol", "Lluvia", "Nieve"]; eje_y = [nsol, nlluvia, nnieve]
plt.bar(eje_x, eje_y, color = ["y","lightblue","grey"]) ; plt.ylabel("Frecuencia") ; plt.xlabel("Clima") ; plt.title("El tiempo en Seattle") ; plt.savefig("Parte2/imagen_grafico/El tiempo en Seattle.jpg"); plt.show()
plt.savefig("Parte2/imagen_grafico/El tiempo en Seattle.png")
