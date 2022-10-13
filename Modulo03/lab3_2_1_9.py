'''
3.2.1.9 LABORATORIO: La sentencia break - Atascado en un bucle

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese 
una palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, 
en cuyo caso el mensaje "¡Has dejado el bucle con éxito". 
Debe imprimirse en la pantalla y el bucle debe terminar.
'''

#Creacion del ciclo whule
while True:
    #Se le pide al usuario ingresar la palabra
    word = input("Ingresa la palabra ")
    #Si la palabra es chupacabras se rompe el ciclo
    if word == "chupacabra":
        break
#Se imprime el mensaje de que se ha roto el ciclo
print("\n¡Has dejado el bucle con éxito!")