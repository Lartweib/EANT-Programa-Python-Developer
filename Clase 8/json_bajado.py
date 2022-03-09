import requests
import json
import pprint

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)
pprint.pprint(objeto)
pprint.pprint(objeto['features'][0]['properties']['NOMBRE'])
