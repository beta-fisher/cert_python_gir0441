'''
 3.4.1.6 LABORATORIO: Lo básico de las listas

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Escribir un programa para listas
'''
hat_list = [1,2,3,4,5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2] = int(input("Ingrese un número: "))

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[len(hat_list) - 1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista:", len(hat_list))

print(hat_list)