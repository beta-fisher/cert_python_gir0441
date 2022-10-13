'''
3.2.1.15 LABORATORIO: Hipótesis de Collatz 

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Escribe un programa que lea un número natural y ejecute los pasos anteriores 
siempre que c0 sea diferente de 1.
'''
def Collatz(numero):
    pasos = 0
    while numero != 1:
        if numero%2==0:
            numero /= 2
            print(int(numero))
            pasos +=1
        else:
            numero = 3*numero + 1 
            print(int(numero))
            pasos+=1
    print("Pasos =",pasos)
    
    

numero = int(input("Ingrese un número: "))
Collatz(numero)

