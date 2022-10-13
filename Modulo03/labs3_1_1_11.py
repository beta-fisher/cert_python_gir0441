'''
3.1.1.11 LABORATORIO: Fundamentos de la sentencia if-else 

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Calculadora de impuestos
'''


#El programa pedira al usuario su ingreso anual 
income = float (input("Introduce el ingreso anual: "))
tax = 0.0

#El programa comparara su respuesta con un valor y dependiendo de este le hara el calculo 
if income < 85528:
    tax = income * 0.18 - 556.02
    print("extension fiscal")
else:
    tax = 14839.02 + ((income - 85528) * 0.32)

#Ahora con el resultado del impuesto si este es menor a cero no se le agregara impuesto porque es un pais feliz
if tax > 0:
    tax = round(tax, 0)
    print("El impuesto es:", tax, "pesos")
else:
    tax = (0.0)
    print("El impuesto es:", tax, "pesos")