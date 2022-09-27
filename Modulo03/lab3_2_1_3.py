'''
Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022
'''

secret_number = 777
number= int(input("Ingresa tu numero "))

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
