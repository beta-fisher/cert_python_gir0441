'''
3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto 

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Crear un programa con un bucle hasta que el usuario adivine el numero
'''
#Se ingresa el valor a la variable que tendra que adivinar luego el usuario y se le pide que ingrese una cantidad
secret_number = 777
number= int(input("Ingresa tu numero "))

#Imprime la introducción al juego
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
#Se le pide al usuario que adivine el numero guardandolo en la variable number
number=int(input())

#El ciclo while comienza y menciona que si la variable secret_number no es igual a numer le mandara el mensaje
#El ciclo se repitira hasta que el usuario ingrese correctamente el numero que sea igual a secret_number
while secret_number != number:
    print("Ja, ja! Estas atrapado en mi bucle!")
    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
    number=int(input())

print("\n¡Bien hecho, muggle! Eres libre ahora")    
