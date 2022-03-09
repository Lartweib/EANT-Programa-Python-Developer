import requests
import pprint
import json

key_clima = 'f6aebc1f999ab9b6a8685e0d60bd5373'
key_geo = '21ea4ad5cbae4cc19041e1fad3f32f91'

archivo_in = open('sucursales_sol_360.csv')
log_error = open('sol360_log_error.txt', 'w')

for linea in archivo_in:
    linea = linea.split(';')
    ciudad_cod = requests.utils.quote(linea[0]) + ',Argentina'
    url = 'https://api.opencagedata.com/geocode/v1/json?q=' + ciudad_cod + '&language=es&key=' + key_geo
    objeto = json.loads(requests.get(url).text)
    lat = objeto['results'][0]['geometry']['lat']
    lon = objeto['results'][0]['geometry']['lng']
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='\
        + str(lat) + '&lon=' + str(lon) + '&units=metric&lang=es&appid=' + key_clima
    objeto = json.loads(requests.get(url).text)
    if objeto.get('weather') == None:
        log_error.write(linea[0] + " no encontrada\n")
    else:
        print(linea[0])
        print('Descripción:', '\t', objeto.get('weather')[0]['description'])
        print('Temperatura:', '\t', objeto.get('main')['temp'], '° C')
        print('Humedad:', '\t\t', objeto.get('main')['humidity'], '%')


log_error.close()
