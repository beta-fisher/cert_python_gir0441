'''
Descripción: Programa el tremendo SAT
Autor: Angel Armando Ramírez Vázquez
Fecha: 11 octubre 2022
'''

ISR = float(input("Ingrese ISR declarado: \n"))

if(ISR < 0):
    print("Solo se permiten valores positivos mayores a cero")
elif (ISR <= 10000):
    A = ISR * 0.05
    print("Su intereses de ISR debe de ser: ", A)
elif(ISR >= 10000 & ISR <= 20000):
    B = ISR * 0.15
    print("Su intereses de ISR debe de ser: ", B)
elif(ISR >= 20000 & ISR <= 35000):
    C = ISR * 0.2
    print("Su intereses de ISR debe de ser: ", C)
elif(ISR >= 35000 & ISR <= 60000):
    D = ISR * 0.3
    print("Su intereses de ISR debe de ser: ", D)
elif(ISR > 60000):
    E = ISR * 0.45
    print("Su ISR más intereses debe de ser: ", E)
