import json
import pprint

with open('perro.json') as archivo:
   objeto = json.load(archivo)
pprint.pprint(objeto.get('perro').get('le_gusta')[0])