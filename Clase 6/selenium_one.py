from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
driver.get("https://es.wikipedia.org/wiki/MacOS#Versiones")

tabla = driver.find_element_by_class_name('wikitable')

filas = tabla.find_elements_by_tag_name('tr')

string_csv = 'Versión,Nombre en código,Anuncio,Presentación,Versión más reciente\n'

for i in range(1, len(filas)):

    valores = filas[i].find_elements_by_tag_name('td')
    string_csv += valores[0].text + ',' + valores[1].text + ',' + valores[2].text + ',' + valores[3].text + ',' + valores[4].text + '\n'

# Introducimos el csv en un archivo
csv = open('macos.csv', 'w')
csv.write(string_csv)
csv.close()
driver.quit()
