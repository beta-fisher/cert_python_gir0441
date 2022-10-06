''' 
Problema 2 Número divisible entre otro
 Realiza un programa en Python que indique si un número es divisible entre otro.
 Nombrar el archivo u1_prob2.py
Ejemplos
Ingresa primer número 5
Ingresa segundo número 3

Resultado
El 5 no es divisible entre 3

Ingresa primer número 12
Ingresa segundo número 6

Resultado
El 12 es divisible entre 6
'''

A = (int(input("Ingresa el primer numero: ")))
B = (int(input("Ingresa el segundo numero: ")))

res = A % B

if isinstance(res, (int))== 0:
    print("El", A, " es divisible entre ", B) 
else:
    print("El", A, " no es divisible entre ", B)
