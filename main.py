import pandas as pnd
import numpy as np

if __name__ == '__main__':
        datos = pnd.read_csv("2a Parte/seattle-weather.csv", header=0 , sep =",")
        lista_tiempo = list(datos["weather"])
        observaciones = pnd.DataFrame({'TIEMPO': lista_tiempo})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['TIEMPO'])
        stats.analisisCaracteristica()
