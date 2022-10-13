'''
3.2.1.14 LABORATORIO: Fundamentos del bucle while 

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar 
la altura de la pirámide que se puede construir utilizando estos bloques.
'''
bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while bloques > 0:
    longitudNecesariaDelNivel = altura + 1

    if longitudNecesariaDelNivel <= bloques:
        bloques -= longitudNecesariaDelNivel
        altura += 1
    else:
        break

print("La altura de la pirámide:", altura)