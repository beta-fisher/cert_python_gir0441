'''
Nombre de la API: Google Maps API Geocoding

Descripción de la API: La API Coloca un mapa interactivo o 
                       una panorámica de Street View en tu 
                       página web con la API de Maps Embed

        Autor: Ángel Armando Ramírez Vazquez
        Fecha de creación: 08/11/2002

Más documentación del uso de la API:
        https://developers.google.com/maps/documentation/embed/get-api-key
'''

#Importación de modulos existentes

import urllib.parse
import requests

#Declaración de variables

#REQUEST de google maps
main_api = "https://maps.googleapis.com/maps/api/geocode/json?" 

#Los valores de latitud y longitud que especifican la ubicación para la que deseas obtener la dirección más cercana en lenguaje natural.
#Geocodificación inversa: Ubicación de brooklyn 
#lat = input("Ingrese su latitud a la que se encuentra ejempo 40.714224: ")     
#lng = input("Ingrese su latitud a la que se encuentra ejempo -73.961452: ")
#API key de google maps 
key="AIzaSyDrQ9VLRoR7kzlwBXaYCBhd1BGrBZiFbIA" 

#CICLO INFINITO while True

while True:
    print()
    print('========================================================================')
    print("Nombre de la API: Google Maps API Geocoding")
    print('========================================================================\n')

    lat = input("Ingrese su latitud a la que se encuentra ejempo 40.714224: \n") 
    if lat =="salir" or lat == "s" or lat == "S" or lat == "Salir":
        break
    print()
    lng = input("Ingrese su latitud a la que se encuentra ejempo -73.961452: \n")
    if lng == "salir" or lng == "s" or lng == "S" or lng == "Salir":
        break
    url = (main_api+'latlng='+lat+","+lng+'&'+'key='+key+"\n")    
    print("URL: ",url)    

    json_data = requests.get(url).json()
    #print(json_data)
    json_status = json_data['status']
    #print(json_status)
    
    
    if str(json_status) == "OK":
            print()
            print('========================================================================')
            print("API Status: " + str(json_status) + " = A successful route call.\n")

            print('========================================================================\n')
            print('Direcciones cercanas en el map View de donde se encuentra : \n')
            for e in json_data['results']:
               # print(e)
                
                  print(e['formatted_address'])            
                  print()
            #print("pagina web: " + str(json_data["articles"]["0"]["author"]))
                                   
    elif str(json_status) == "INVALID_REQUEST":
                print("**********************************************")
                print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
                print("**********************************************\n")
                print("=============================================")
    else:
                print("************************************************************************")
                print("For Staus Code: " + str(json_status) + ", Refer to:")
                print("https://developers.google.com/maps/documentation/embed/get-api-key")
                print("************************************************************************\n")   


    
#latlng=lat+','+lng Prueba que se realizo para testear si con esto el modulo urlib nos creaba bien la url
#print(latlng)

#Creación de la URL con apoyo del modulo 
#url=main_api + urllib.parse.urlencode({"latln":latlng,"key":key})

#Impresión de url, herramienta de apoyo para verificar que la impresión de URL sea correcta
#print (url," \n")

#Asignación de restful request a la variable url
#url = (main_api+'latlng='+lat+","+lng+'&'+'key='+key)
#print(url,'\n')





