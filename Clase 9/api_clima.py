import requests
import pprint
import json

key = 'f6aebc1f999ab9b6a8685e0d60bd5373'

ciudad  = "San Juan, Argentina"
ciudad_cod = requests.utils.quote(ciudad)

url = 'http://api.openweathermap.org/data/2.5/weather?q='  + ciudad_cod + '&lang=es&appid=' + key

objeto = json.loads(requests.get(url).text)
#pprint.pprint(objeto)

descripcion  = objeto['weather'][0]['description']

pprint.pprint(descripcion)
