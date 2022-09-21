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


tiempos = leerArchivo('seattle-weather.csv')['weather'].tolist()
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
#probabilidades relacionadas(definen el modelo de markov)
