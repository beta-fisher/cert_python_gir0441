'''
4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones
Autor: Angel Armando Ramirez Vazquez
Fecha: 4 sep 2022

Escribir y probar una función que toma un argumento (un año) y devuelve True 
si el año es un año bisiesto, o False si no lo es.
'''

#Se escribe la función que se podra invocar en otro momento
def is_year_leap(year):
    Bisiesto = False
    diviEntre_4 = year % 4
    diviEntre_100 = year % 100
    diviEntre_400 = year % 400

#If anidado en el cual el primer parametro es que sea mayor o igual a 1582 
#En el cual evaluara si al dividirlo entre 4 el residuo no es igual en dado caso no es bisiesto
    if year >= 1582:
        if diviEntre_4 != 0:
            Bisiesto = False
#El siguiente que utilizamos es elif para ver si el residuo entre 100 y 4 nos da que es verdadero
        elif diviEntre_100 != 0:
            Bisiesto = True
#Siguiendo de lo anterior si se puede ver el residuo entre 400 este si es bisiesto
        elif diviEntre_400 != 0:
            Bisiesto = False
#El else de elif que nos dira que si en evaluación de las otras opciones no se cumpla pasara a él
        else:
            Bisiesto = True
#El else del if que nos dara el resultado de false en dado caso que las demás ya no se cumplan
    else:
        Bisiesto = False
#Return que nos devolvera nuestro resultado y terminara con nuestro if anidado
    return Bisiesto

#Lista de argumentos con los que se probara el programa
test_data = [1900, 2000, 2016, 1987]
#Lista de resultados con los cuales debe ser la salidad
test_results = [False, True, True, False]
#Ciclo for con el cual se evaluaran los argumentos de la primera lista 
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
#Impresión del resultado dependiendo su naturaleza 
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
