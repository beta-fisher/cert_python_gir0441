'''
Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022
'''

year = int(input("Introduce un año: "))

if year % 4 != 0: #No es divisble entre 
    print('Año común')
elif year % 100 != 0: #Año bisiesto
    print('Año bisiesto')
elif year % 400 != 0:
        print('Año común')
else:
    print("Es un año bisiesto")