from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
#import mysql.connector

#op = webdriver.ChromeOptions()
#op.add_argument('headless')

driver = webdriver.Chrome("./chromedriver.exe") #,options=op)
url = 'https://supermercado.carrefour.com.ar/catalogsearch/result/?q=cerveza'
driver.get(url)

js_scroll_dar_posicion = '''
        fin_de_pantalla = document.body.scrollHeight
        window.scrollTo(0, fin_de_pantalla)
        return fin_de_pantalla
        '''
aprieta_boton = '''
        boton = document.querySelector('[class="ver-mas-productos btn meanbee-infinitescroll-button"]').click()
        '''
existe_boton =  '''
        boton = document.querySelector('[class="ver-mas-productos btn meanbee-infinitescroll-button"]')
        if (boton){
                return 'Existe'
        } else {
                return 'No existe'
        }
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
   if driver.execute_script(existe_boton) == 'Existe':
       driver.execute_script(aprieta_boton)
       sleep(3)
print("Llegamos al final de la página")

#====================================================================
#====================================================================
#====================================================================
archivo_out = open('productos_carrefour.csv','w',encoding = 'utf-8')
archivo_out.write('ID_DESCRIPCION_MARCA_PRECIO PUBLICADO_PROMOCION_PRECIO POR LITRO_TIPO DE PRODUCTO\n')

#r = driver.find_elements_by_xpath('//p[@class="brand truncate"]')
r = driver.find_elements_by_xpath('//a[@class="open-modal"]/img')

#sleep(3)
time = 3
for i in range(len(r)):
    try:
        r[i].click()
        sleep(time)
        html = driver.execute_script('return document.documentElement.outerHTML')
        dom = BS(html , features = 'html.parser')
        productos = dom.find_all(class_="product-essential")
        #print(productos)
        
        descripcion = productos[0].find(class_='h1').text
        marca = ' '.join(productos[0].find(class_="brand truncate").text.strip('\n').split())
        
        try:
            precio_publicado = productos[0].find(class_="precio-numero truncate").text.replace('$','')
        except:
            precio_publicado = productos[0].find(class_="price 207 precio-regular-productos-destacados").text.replace('$','').replace(' ','').replace('\n','')
        
        try:
            promocion = productos[0].find(class_="price precio-oferta-productos-destacados").text.strip('\n').split()
            promocion_f = (promocion[1] + ' ' + promocion[2])
        except:
            promocion_f = 'N/A'
        
        precio_por_litro = productos[0].find(class_="precio-unidad").text.split('$')[1].split()[0]
        tipo_de_producto = ' '.join(productos[0].find_all(class_="info")[1].text.strip('\n').split())
        
        close = driver.find_element_by_xpath('//*[@id="modalProduct"]/div[1]/i')
        id_ = i+1
        archivo_out.write(str(id_) + '_' + descripcion + '_' + marca + '_' + precio_publicado + '_' + promocion_f + '_' + precio_por_litro + '_' + tipo_de_producto + '\n')
        
        print(i+1)
        print(descripcion)
        print(marca)
        print(precio_publicado)
        print(promocion_f)
        print(precio_por_litro)
        print(tipo_de_producto)
        print('=================')
        
        close.click()
        sleep(time)
        
    except: continue


archivo_out.close()
print('Archivo creado')

#====================================================================
#====================================================================
#====================================================================

