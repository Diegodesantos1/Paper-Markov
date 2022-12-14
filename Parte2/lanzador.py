import pandas as pnd
import Parte2.JMPEstadisticas as jmp
import numpy as np
import matplotlib.pyplot as plt
from Parte2.algoritmo import Markov
from introducir import solicitar_introducir_numero_extremo

def main():
        eleccion=solicitar_introducir_numero_extremo("¿Qué quieres ejecutar? 1: Análisis de datos, 2: Algoritmo y análisis de Markov, 3 DTW, 4 Fin", 1, 4)
        if eleccion==1:
                variables = ["precipitation","temp_max","temp_min","wind"]
                for i in range (4):
                        variable = variables.pop(0)
                        datos = pnd.read_csv("Parte2/Industry4.0.csv", header=0 , sep =",")
                        lista_tempmax = list(datos[f"{variable}"])
                        observaciones = pnd.DataFrame({'VARIABLE': lista_tempmax})
                        #--- ANALISIS DE UNA CARACTERISTICA ---
                        stats = jmp.JMPEstadisticas(observaciones['VARIABLE'])
                        stats.analisisCaracteristica()
                main()
        if eleccion==2:
                Markov.test()
                main()
        if eleccion==3:
                import Parte2.algoritmos
        if eleccion==4:
                print("Fin del programa")
                exit()