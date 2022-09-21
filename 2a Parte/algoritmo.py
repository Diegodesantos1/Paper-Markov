import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
# leemos el archivo csv
def leerArchivo(csv):
    df = pd.read_csv(csv)
    return df

#print(leerArchivo('police_deaths.csv'))
df1 = leerArchivo('police_deaths.csv')
frecuencia = df1.groupby(['Year']).count()
#print(frecuencia)

frecuencia.plot(kind='line', color='black')
#plt.show()

def k9Unit(df):
    df = df[df['K9_Unit'] == 1]
    return df

#print(k9Unit(df1))
df2 = k9Unit(df1)

def muertesPorAño(df):
    df = df.groupby(['Year']).count()
    return df

#print(muertesPorAño(df2))


tiempos = leerArchivo('2a Parte/seattle-weather.csv')['weather'].tolist()
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
        return [v_s, v_ll, v_n]
    else:
        return [nv_s, nv_ll, nv_n]

#probabilidad de una secuencia de estados(los definidos aleatoria)
def markov(secuencia):
    lista1 = []
    lista2 = []
    lista3 = []
    listadefi = []
    contador = 0
    for i in range(len(secuencia)):
        if contador == 0:
            a1 = sacar_valor(secuencia[contador])[0]*prob_sol
            a2 = sacar_valor(secuencia[contador])[1]*prob_llu
            a3 = sacar_valor(secuencia[contador])[2]*prob_niev
            lista1.append(a1)
            lista2.append(a2)
            lista3.append(a3)
        else:
            a1 = sacar_valor(secuencia[contador])[0]*(m_t[0][0]*lista1[contador-1]+m_t[1][0]*lista2[contador-1]+m_t[2][0]*lista3[contador-1])
            a2 = sacar_valor(secuencia[contador])[1]*(m_t[0][1]*lista1[contador-1]+m_t[1][1]*lista2[contador-1]+m_t[2][1]*lista3[contador-1])
            a3 = sacar_valor(secuencia[contador])[2]*(m_t[0][2]*lista1[contador-1]+m_t[1][2]*lista2[contador-1]+m_t[2][2]*lista3[contador-1])
            lista1.append(a1)
            lista2.append(a2)
            lista3.append(a3)
        contador+=1
    listadefi.append[lista1[len(lista1)-1]]
    listadefi.append[lista2[len(lista2)-1]]
    listadefi.append[lista3[len(lista3)-1]]
    return listadefi