'''
Author: ÁNGEL ARMANDO RAMIREZ VAZQUEZ
Fecha: 25/octubre/2022

'''

#Importación de librerías existentes

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "México"
key  = "RviDNX6lvy58NDKYBhxHATAC6kjDZ4Z9"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data) 