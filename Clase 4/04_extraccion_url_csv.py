import requests

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text

archivo = open('peliculas.csv', 'w')
archivo.write(contenido)
archivo.close()