import json
import requests
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'

objeto = json.loads(requests.get(url).text)

# for i in range(len(objeto['features'])):
#     print(objeto['features'][i])

bd = cliente['salud']
coleccion = bd['estaciones']
coleccion.insert_many(objeto['features'])