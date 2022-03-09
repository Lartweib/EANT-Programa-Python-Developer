import requests
import json
import pprint

direccion = "Rivadav 6300"
localidad = 'caba'
print(direccion + ', ' + localidad)

direccion_formato = requests.utils.quote(direccion + ', ' + localidad)
print(direccion_formato)

url = 'http://servicios.usig.buenosaires.gob.ar\
/normalizar/?geocodificar=True&direccion=' + direccion_formato
print(url)

dir_normalizada = json.loads(requests.get(url).text)
pprint.pprint(dir_normalizada)