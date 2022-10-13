'''
4.3.1.9 LABORATORIO: Números primos: ¿Cómo encontrarlos?

Autor: Angel Armando Ramirez Vazquez
Fecha: 4 sep 2022

Imprime los numeros primos que existan en un rango de 1 a 20
'''

#Se crea la función con la cual se evaluara si el numero es primo o no
def is_prime(num):
#Tomamos como referencia "2"  
    div = 2
#El ciclo while se iniciara en cuanto la variable div sea menor
    while div < num:
#Si el residuo de num y div es cero este no sera y se hara un incremento a div
        if num % div == 0:
             return False
        div += 1
#En dado caso que el residuo sea distinto a 0 este sera un numero primo y devolvera el valor True
    return True

#Se realiza un ciclo for con el cual los rangos que ingresamos empieza con 1 y termina con 20 
#Y se imprimira los numeros que resulten ser primos 
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()