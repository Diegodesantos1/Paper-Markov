import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# leemos el archivo csv
def leerArchivo():
    df = pd.read_csv('Industry4.0.csv')
    return df

def calculoMediaAritmetica(caracteristica):
    n = caracteristica.count()
    sumaValoresObservaciones = 0
    mediaAritmetica = 0
    for valorObservacion in caracteristica:
        sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion
    mediaAritmetica = sumaValoresObservaciones / n
    return mediaAritmetica
print(calculoMediaAritmetica(leerArchivo()["Tot Deaths/1M pop"]))

