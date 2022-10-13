'''
3.2.1.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales 

Autor: Angel Armando Ramirez Vazquez
Fecha: 29 sep 2022

Crear un programa que al ingrresar una palabra este la imprima sin las vocales 
'''

#Se crea la funcion con upper para que este convierta las letras en mayusculas
def devorador(entrada):
    entrada = entrada.upper()

#Se crea el ciclo for con la cual si la entrada contiene alguna de las vocales las omite
    for letra in entrada:
        if letra == "A" or letra=="E" or letra =="I" or letra =="O" or letra =="U":
            continue
        else:
            print(letra, end=' ')

#Imprime el resultado
entrada = input("Ingrese la palabra: ")
devorador(entrada)
