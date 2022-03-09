from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe") 
driver.get('https://www.olx.com.ar/libros-y-revistas_c860')

for i in range(0,3):

    boton=driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    
    boton.click()
    
    time.sleep(5)

title=driver.find_elements_by_xpath('//span[@data-aut-id="itemTitle"]')
for titulos in title:
    print(titulos.text)
    
driver.quit()
