import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features='html.parser')
articulos = dom.find_all('article')
#Exploro el elemento
print(articulos[0].figure.div.a['title'])

for lib in range(10):
   print(articulos[lib].figure.div.a['title'])