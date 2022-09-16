"""import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

if __name__ == '__main__':
        datos = pnd.read_csv("Industry4.0.csv", header=0 , sep =",")
        lista_poblacion = list(datos["Population"])
        observaciones = pnd.DataFrame({'POBLACION': lista_poblacion})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['POBLACION'])
        stats.analisisCaracteristica()
"""