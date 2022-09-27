'''
Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022
'''
income = float (input("Introduce el ingreso anual: "))

tax = 0.0

if income < 85528:
    tax = income * 0.18 - 556.02
    print("extension fiscal")
else:
    tax = 14839.02 + ((income - 85528) * 0.32)

    
tax = round(tax, 0)
print("El immpuesto es:", tax, "pesos")