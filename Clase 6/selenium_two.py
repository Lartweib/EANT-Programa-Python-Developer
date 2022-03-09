import random
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome("chromedriver")

driver.get('https://www.olx.com.ar/libros-y-revistas_c860')

script_js = """
    setTimeout(function(){
        document.querySelector('[data-aut-id="btnLoadMore"]').click()
    }, 5000)
"""

for i in range(3): # Hacer click en "Cargar más" 3 veces
    try:
        # Esperar que se cargue la pagina
        sleep(random.uniform(8.0, 10.0) )

        # Buscar con JS el boton para cargar mas informacion
        driver.execute_script( script_js )

        # Esperar que se carguen los items dinámicamente
        sleep(random.uniform(8.0, 10.0) )
    except:
        # Si hay algun error... frenar el ciclo
        break

# Buscar con XPATH cada item donde esta la informacion que voy a extraer
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
