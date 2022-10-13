'''
3.2.1.6 LABORATORIO: Fundamentos del bucle for: el conteo

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Usar un ciclo for con time.sleep para que imprima la sentencia Mississippi
'''

import time
# scribe un bucle for que cuente hasta cinco.

for i in range(1,6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(i,"Mississippi")
    # Cuerpo del bucle - usar: time.sleep (1)
    time.sleep(1)

# Escribe una función de impresión con el mensaje final.
print("¡Listos o no, ahí voy!")