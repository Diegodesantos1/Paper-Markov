import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

variables = ["precipitation","temp_max","temp_min","wind"]
for i in range (4):
        variable = variables.pop(0)
        datos = pnd.read_csv("Parte2/seattle-weather.csv", header=0 , sep =",")
        lista_tempmax = list(datos[f"{variable}"])
        observaciones = pnd.DataFrame({'VARIABLE': lista_tempmax})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['VARIABLE'])
        stats.analisisCaracteristica()
