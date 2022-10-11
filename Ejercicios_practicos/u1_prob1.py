'''
Descripción: Cuenta de ahorro
Autor: Angel Armando Ramírez Vázquez
Fecha: 11 octubre 2022
'''

A = int(input("Ingrese la cantidad de dinero depositado: \n"))

year_one    = (A + (A * 0.04))
year_two    = (year_one + (year_one * 0.04))
year_three  = (year_two + (year_two * 0.04))


print("El Ahorra tras el primer año es de: ",float('{0:.5}'.format(year_one)))
print("El Ahorra tras el segundo año es de: ",float('{0:.5}'.format(year_two)))
print("El Ahorra tras el tercer año es de: ",float('{0:.5}'.format(year_three)))
