import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'
respuesta = requests.get(url)

print('código de respuesta', respuesta.status_code)
print('URL: ', respuesta.url)
print('contenido "crudo:', respuesta.content)
print('como texto:', respuesta.text)
print('codificación:', respuesta.encoding)
respuesta.encoding = 'utf-8'
print('como texto:', respuesta.text)
