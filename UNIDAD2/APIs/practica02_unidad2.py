'''
Nombre de la API: Yelp fussión research

Descripción de la API: Este punto final devuelve hasta 1.000 
                       empresas en función de los criterios de 
                       búsqueda proporcionados. 
                       Contiene información básica sobre el negocio. 

        Autor: Ángel Armando Ramírez Vazquez
        Fecha de creación: 08/11/2002

Más documentación del uso de la API:
        https://www.yelp.com/developers/documentation/v3/business_search
'''

#Importación de modulos existentes

import urllib.parse
import requests

#Declaración de variables

#REQUEST de Yelp fusión
main_api = "https://api.yelp.com/v3/businesses/search" 

#Variables dinamicas
#print("Escriba su localidad")
#print("Ejemplo: New York City, NYC 350 5th Ave, New York, NY 10118")
#localidad=input()


#Parametros (Estos parametros son obligatorios que nos pide la API)
#En esta caso usamos la direcciónd eprueba de Yelp que es una ubicación de New york
#parameters={"location":localidad,
#            "term":"Mall",
#            "radius":5000,
#            "limit":3}

#API key de Yelp fusión 
key="D6fU3bNCpEyD5AhK_lyiKYGRihzgPy3ktlh4PHNQWs5YjOiPr1Ug5ZuBt3Tc7hhhBEg-IhV5whROlGG9xuiYSXm7_im_Zj2Jpu6SuKFbgq8PzomWPC5cvnWIazVrY3Yx" 

#Headers
headers={"Authorization":"Bearer %s" % key}

while True:
    print()
    print("Nombre de la API: Yelp fussión research\n")
    #Variables dinamicas
    print("Escriba su localidad \n")
    print("Ejemplo: New York City, NYC 350 5th Ave, New York, NY 10118 \n")    
    localidad=input()
    localidad_string=str(localidad)
    if localidad =="salir" or localidad == "s" or localidad == "S" or localidad == "Salir":
        break
    print("Escriba ejemplos de negocios\n")
    print("Ejemplo Mall\n") 
    negocio=input()
    negocio_string=str(negocio)
    if negocio =="salir" or negocio == "s" or negocio == "S" or negocio == "Salir":
        break
    parameters={"location":localidad,
                "term":negocio,
                "radius":5000,
                "limit":3}
    print()  
    url_status = requests.get(main_api, headers=headers, params=parameters)
    print(url_status,'\n')
   
    
    
    if str(url_status) == "<Response [200]>":
            print("API Status: " + str(url_status) + " = A successful route call.\n")
             #AQUI SE AGREGARA LA INFORMACIÓN OBTENIDA
            query = url_status.json()['businesses']
            for q in query:
                print("Negocios cercanos")
                print('==================================================================================')                   
                print("Mall: {}".format(q['name']))
                print("Rating: {}".format(q['rating']))
                print('==================================================================================')  
    elif str(url_status) == "<Response [400]>":
                print("**********************************************")
                print("For Staus Code: " + str(url_status) + "; Invalid user inputs for one or both locations.")
                print("**********************************************\n")
                print("=============================================")
    else:
                print("************************************************************************")
                print("For Staus Code: " + str(url_status) + ", Refer to:")
                print("https://www.yelp.com/developers/documentation/v3/business_search")
                print("************************************************************************\n")



#Creación de la URL con apoyo del modulo 
#url=main_api + urllib.parse.urlencode({"headers":headers, "params":parameters})

#Impresión de url, herramienta de apoyo para verificar que la impresión de URL sea correcta
#print (url)

#Declaración de la variable url que alamacena los valores del restful 
#url = requests.get(main_api, headers=headers, params=parameters)
#print(url,'\n')

#print(json_data) 
#json_data = url.json()
#print(json_data)

