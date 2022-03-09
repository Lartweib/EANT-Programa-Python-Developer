import requests
import csv
from io import StringIO

url = ''
respuesta = requests.get(url)
contenido = respuesta.text
archivo_str = StringIO(contenido)

objeto_csv = csv.reader(archivo_str)

archivo = open('peliculas_mod_google.csv', 'w')
for linea in objeto_csv:
   archivo.write(linea[0] + ',' + linea[2] + ',' +  linea[1] + '\n')

archivo.close()