'''
4.3.1.10 LAB: Convirtiendo el consumo de combustible

Autor: Angel Armando Ramirez Vazquez
Fecha: 5 sep 2022

Convierte el consumo de gasolina de litros por cada 100 km a millas por galón
y viceversa
'''

#Función que convierte litros por 100 km a millas por galon
def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784 
    return miles / gallons

#Función que convierte millas por galon a litros por 100 km  
def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784 
    km = miles * 1609.344 / 1000 
    km100 = km / 100
    return liters / km100

#Impresión de los resultados según los datos a evaluar
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))