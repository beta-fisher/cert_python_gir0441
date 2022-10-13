'''
4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones
Autor: Angel Armando Ramirez Vazquez
Fecha: 4 sep 2022

Escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve 
el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, 
tu función debería ser universal).
'''

#Función creada para poder evaluar y verificar que cumple con los requisitos 
#esto se hace con la finalidad de saber si el año es bisiesto o no y ver si afecta a febrero 
#hasta el final nos retorne el resultado
def isYearLeap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

#Función creada por nosotros con la cual tomara el numero de dias dependiendo del año
def daysInMonth(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if isYearLeap(year)==True and month==2:
        return 29
    else:
        return months[month-1]

#Listas con los datos a evaluar 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
#Ciclo for con el cual se pasaran los datos y nos dara los resultados
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
#Impresión de resultados
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")