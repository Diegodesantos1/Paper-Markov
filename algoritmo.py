import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# leemos el archivo csv
def leerArchivo(csv):
    df = pd.read_csv(csv)
    return df

print(leerArchivo('police_deaths.csv'))
df1 = leerArchivo('police_deaths.csv')
frecuencia = df1.groupby(['Year']).count()
print(frecuencia)

frecuencia.plot(kind='line', color='black')
plt.show()

def k9Unit(df):
    df = df[df['K9_Unit'] == 1]
    return df

print(k9Unit(df1))
df2 = k9Unit(df1)

def muertesPorAño(df):
    df = df.groupby(['Year']).count()
    return df

print(muertesPorAño(df2))