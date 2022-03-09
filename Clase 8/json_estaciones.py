import requests
import json
import pprint
#Capturo el JSON
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)
#Creo el archivo de salida
archivo_out = open('estaciones_sal.csv', 'w')
#Títulos
archivo_out.write('latitude,longitude,name,label\n')

for i in range(len(objeto['features'])):
    latitude = (objeto['features'][i]['geometry']['coordinates'][1])
    longitude = (objeto['features'][i]['geometry']['coordinates'][0])
    nombre = (objeto['features'][i]['properties']['nombre'])
    direccion = (objeto['features'][i]['properties']['ubicacion'])
    archivo_out.write(str(latitude) + ',' + str(longitude) + ',' + direccion + ',' + nombre + '\n')

archivo_out.close()