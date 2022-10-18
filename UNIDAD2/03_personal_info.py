'''
 Author: Angel Armando Ramírez Vázquez
 Personal info: Programa pregunta piezas de informació y las imprime
 18 de octubre 2022
'''

#El space en el documento decia variable pero la puse como constante
space = " "
#Asignaciónd de valores por parte del usuario por proceso de pregunta
name = input("¿Cuál es su nombre? ")
lastname = input("¿Cuál es su apellido? ")
location = input("¿Donde vive? ")
age = input("¿Qué edad tiene usted? ")

#Impresion con concatenación
print("Hola!", name, lastname, "de", location, "y tiene", age, "años")
print("Hola!",space,name,space,lastname,space,"de",space,location,space,"y tiene",space,age,space,"años")