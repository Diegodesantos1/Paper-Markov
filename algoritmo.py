import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# leemos el archivo csv
def leerArchivo(csv):
    df = pd.read_csv(csv)
    return df

print(leerArchivo('police_deaths.csv'))
df = leerArchivo('police_deaths.csv')
frecuencia = df.groupby(['Year']).count()
print(frecuencia)

frecuencia.plot(kind='line', color='black')
plt.show()
