from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:/Users\gonza\Desktop\PDD L-M\Clase 6\chromedriver.exe')
url = 'https://www.lanacion.com.ar/'
driver.get(url)

js_scroll_dar_posicion = '''
   fin_de_pantalla = document.body.scrollHeight
   window.scrollTo(0, fin_de_pantalla)
   return fin_de_pantalla
'''
sleep(3)
pos_actual = 0
pos_siguiente = driver.execute_script(js_scroll_dar_posicion)
sleep(3)
while pos_actual != pos_siguiente:
   pos_siguiente = pos_actual
   pos_actual = driver.execute_script(js_scroll_dar_posicion)
   sleep(3)
   print(pos_actual)
print("Llegamos al final de la página")