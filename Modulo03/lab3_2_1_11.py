'''
3.2.1.11 LABORATORIO: La sentencia continue - El Bonito Devorador de Vocales 

Autor: Angel Armando Ramirez Vazquez
Fecha: 27 sep 2022

Crear un programa que al ingrresar una palabra este la imprima sin las vocales 
'''


palabraSinVocal = ""
userWord = ""

#El usuario ingresa una palabra y se convierte a mayusculas
userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

#Entrea en un ciclo for que funciona con if y elif 
for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal += letra

#Se imprime la palabra sin vocales
print(palabraSinVocal)