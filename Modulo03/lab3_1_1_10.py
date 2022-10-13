'''
 3.1.1.10 LABORATORIO: Operadores de comparación y ejecución condicional

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada
'''

#La variable "planta" obtiene el valor ingresado por el usuario
planta = input ('Ingresa el nomnbre de la planta ')

#Con el valor de planta entrara al if comparandolo y si rsulta ser igual esta imprimira el resultado 
if planta == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
if planta == "espatifilo" :
    print("No, ¡quiero un gran ESPATIFILIO!")
if planta == "pelargolino" :
    print("¡ESPATIFILIO!, ¡No pelargolino!")