from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:/Users\gonza\Desktop\PDD L-M\Clase 6\chromedriver.exe')

driver.get('https://www.olx.com.ar/items/q-aspiradoras')

#js_hola = "alert('Hoooolaaaa')"

js_clickear_boton = """        
    boton = document.querySelector('[data-aut-id="btnLoadMore"]')
    boton.click()   
"""

js_preguntar_boton = """        
    boton = document.querySelector('[data-aut-id="btnLoadMore"]')
    if (boton){
        return "Existe"
    } else{
        return "No existe"
    }   
"""

existe_boton = driver.execute_script(js_preguntar_boton)

while existe_boton == 'Existe':
    driver.execute_script(js_clickear_boton)
    sleep(5)
    existe_boton = driver.execute_script(js_preguntar_boton)
    
###
html = driver.execute_script("return document.documentElement.outerHTML")

###
from bs4 import BeautifulSoup

dom = BeautifulSoup(html, features='html.parser')

articulos = dom.find_all(class_ ='IKo3_')

#articulos = dom.find_all(attrs={'class'='IKo3_'})
print

for articulo in articulos:

    precio =articulo.find(class_ ='_89yzn').text
    titulo =articulo.find(class_ ='_2tW1I').text
    
    print(titulo + " / " + precio)

driver.quit()














