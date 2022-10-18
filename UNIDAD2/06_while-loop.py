'''
 Author: Angel Armando Ramírez Vázquez
 Personal info: Programa pregunta piezas de informació y las imprime
 18 de octubre 2022
'''

#Ingresa el valor a la variable 
x = input("Enter a number to count to: ")
x = int(x)
x = abs(x)
y = 1

#Se imprime un loop que dara como resultado un listado de  1 hasta "x"
while y <= x:
    print(y)
    y=y+1