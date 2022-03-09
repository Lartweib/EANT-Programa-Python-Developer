import requests
import json
import pprint

direccion = input("Ingrese la dirección: ")
localidad = 'caba'
#print(direccion + ', ' + localidad)

direccion_formato = requests.utils.quote(direccion + ', ' + localidad)
#print(direccion_formato)

url = 'http://servicios.usig.buenosaires.gob.ar\
/normalizar/?geocodificar=True&direccion=' + direccion_formato
#print(url)

dir_normalizada = json.loads(requests.get(url).text)
#pprint.pprint(dir_normalizada)
print('Dirección:', dir_normalizada['direccionesNormalizadas'][0]['direccion'])
print('Coordendas:', dir_normalizada['direccionesNormalizadas'][0]['coordenadas'])
coordenadas = dir_normalizada['direccionesNormalizadas'][0]['coordenadas']
x = float(coordenadas['x'])
