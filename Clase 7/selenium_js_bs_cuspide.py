from selenium import webdriver
from time import sleep
from random import randint
from bs4 import BeautifulSoup

def bs():
    html = driver.execute_script("return document.documentElement.outerHTML")
    dom = BeautifulSoup(html, features='html.parser')
    articulos = dom.find_all(class_ ='libro libro')
    for articulo in articulos:
        titulo = articulo.a.get('title')
        precio = articulo.find(class_ ='precio').text.replace('\n', '')
        print(titulo + ': ' + precio)
        
#Versión silenciosa
op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome('C:/Users/gonza/Desktop/PDD L-M/Clase 6/chromedriver.exe', options=op)

driver.get('https://www.cuspide.com/resultados.aspx?c=Biolog%C3%ADa,%20Ciencias%20de%20la%20Tierra(T%C3%A9cnicos)&tema=2173&por=Tema&orden=fecha&pg=1')

js_click_boton = """
    boton = document.querySelector('[title="Siguiente"]')
    if (boton){
            boton.click()
    }else{
        return "Fin Página"
    }
"""
bs()
while driver.execute_script(js_click_boton) != "Fin Página":
    sleep(randint(2,5))
    bs()
