from selenium import webdriver
from time import sleep
from random import randint

driver = webdriver.Chrome("chromedriver.exe") 
driver.get('https://www.olx.com.ar/libros-y-revistas_c860')

for i in range(3):

    boton=driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    
    boton.click()
    
    sleep(randint(3, 5))

items = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Recorrer cada uno de los items encontrados
for item in items:
    # Extraer el precio
    precio = item.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    # Extraer el titulo
    titulo = item.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(titulo)

driver.quit()
