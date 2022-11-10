'''
Nombre de la API: News API

Descripción de la API: Obtenga y busque noticias de más de 30.000 publicaciones 
                       con esta API sencilla y gratuita (para proyectos no comerciales), 
                       puede consultar por palabra clave, publicación o tema. 

        Autor: Ángel Armando Ramírez Vazquez
        Fecha de creación: 08/11/2002

Más documentación del uso de la API:
        https://newsapi.org/docs
'''

#Importación de modulos existentes

import urllib.parse
from urllib.request import urlopen
import requests
import json

#Declaración de variables

#REQUEST de Yelp fusión
main_api = "https://newsapi.org/v2/everything?" 

#Parametros (Estos parametros son obligatorios que nos pide la API)
#En esta caso usamos la direcciónd eprueba de Yelp que es una ubicación de New york
#q=input("Ingrese palabra clave de lo que quiere noticias ejemplo Apple: ") 
#fecha=input("Fecha del dia ejmplo 2022-11-9: ") 
sortBy="popularity"

#API key de Yelp fusión 
key="b9f5d758ae0c48a89e89fb7130830588" 


while True:
    print()
    print("Nombre de la API: News API\n")
    q=input("Ingrese palabra clave de lo que quiere noticias ejemplo Apple: ") 
    if q =="salir" or q == "s" or q == "S" or q == "Salir":
        break
    print()
    fecha=input("Fecha del dia ejmplo 2022-11-9: ") 
    if fecha == "salir" or fecha == "s" or fecha == "S" or fecha == "Salir":
        break
    url=main_api + urllib.parse.urlencode({"q":q,"from":fecha,"sortBy":sortBy,"apiKey":key})   
    print("URL: ",url)    
#print(json_data)
    json_data = requests.get(url).json()
    json_status = json_data["status"]
    print(json_status)
    #print(json_data)

    if str(json_status) == "ok":
            print()
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            
            for e in json_data['articles']:
                  print('\n')
                  print('======================= ARTICULO PUBLICADOS DE '+q+' CON FECHA '+fecha+" ===========================================\n")
                  print('Titulos del artículo: ')
                  print(e['title'])
                  print('\n')
                  print('Nombre del autor: ')
                  print(e['author'])
                  print('\n')
                  print('Descripción de la nota: \n')
                  print(e['description'])
                  print('\n')
                  print('====================================================================================================================\n')
                  
                
            
                
            #print("pagina web: " + str(json_data["articles"]["0"]["author"]))
                                   
    elif str(json_status) == "INVALID_REQUEST":
                print("**********************************************")
                print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
                print("**********************************************\n")
                print("=============================================")
    else:
                print("************************************************************************")
                print("For Staus Code: " + str(json_status) + ", Refer to:")
                print("https://newsapi.org/docs")
                print("************************************************************************\n")



#Creación de la URL con apoyo del modulo 
#url=main_api + urllib.parse.urlencode({"q":q,"from":fecha,"sortBy":sortBy,"apiKey":key})

#Impresión de url, herramienta de apoyo para verificar que la impresión de URL sea correcta
#print (url,'\n')

#print(json_data) 
#json_data = requests.get(url).json()
#print(json_data) 
