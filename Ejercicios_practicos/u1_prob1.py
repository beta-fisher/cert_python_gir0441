'''
Resuelve el siguiente problema de las raíces de una ecuación cuadrática mediante la
fórmula general.
* Escribir un programa en Python donde se utilice funciones.
* Nombrar el archivo u1_prob1.py
* Define función que lee un valor de usuario y regresa valor leído.
* Define función que calcule el resultado √b**2 + 4ac  y regrese su valor lógico que

        x = (-b +- √b**2 + 4ac )/(2a)
*Una vez terminado realiza la prueba ingresando los valores listados, pega tu
    evidencia no olvidando perfil de cuenta de Google o de Cisco.
* Verifica que la salida sólo tenga dos dígitos.
'''

from math import sqrt

A = int(input("Ingrese el valor de a: \n"))
B = int(input("Ingrese el valor de b: \n"))
C = int(input("Ingrese el valor de c: \n"))
x1= 0
x2= 0

if ((B**2)-4*A*C) < 0:
  print("No podemos resolver su ecuación")
else:
  x1 = (-B-sqrt(B**2-(4*A*C)))/(2*A) 
  x2 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  print("RESULTADOS:")
  print("X1 = ",x1)
  print("X2 = ", x2)
  

