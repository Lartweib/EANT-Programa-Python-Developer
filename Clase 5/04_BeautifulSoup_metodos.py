from bs4 import BeautifulSoup

archivo_html = open('web_ejemplo.html', encoding='utf-8')

dom = BeautifulSoup(archivo_html, features='html.parser')

# print(dom.prettify())


#métdos de captura de etiquetas
primer_link = dom.a

print(primer_link.string)

primer_link = dom.find('a')

todos_los_links = dom.find_all('a')

print(todos_los_links)

primer_link = todos_los_links[0]
segundo_link = todos_los_links[1]

#capturando valores en atributos
print(primer_link['class'])
print(primer_link['href'])
print(primer_link['id'])

for link in todos_los_links:
    print(link['href'])
    
    
#Presisando la búsqueda
parrafo_target = dom.find('p', id='otros-integrantes')

parrafo_target = dom.find(id='otros-integrantes')

dom.find_all(class_='nombre-clase')

ultimos_tres_links = parrafo_target.find_all('a')

for link in ultimos_tres_links:
    print(link['href'])





















