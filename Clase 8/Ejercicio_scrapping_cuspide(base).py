from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
import mysql.connector

#==========================================================================

def guardar_en_csv():
    sleep(3)
    html = driver.execute_script('return document.documentElement.outerHTML')
    dom = BS(html , features = 'html.parser')
    libros = dom.find_all(class_='md-datos')
    
    for i in range(len(libros)):
        titulo = dom.find_all(class_='md-datos')[i].a['title']
        precio = dom.find_all(class_='md-precio')[i].find(class_='precio').text.split(' ')[1].split('\n')[0]
        try:
            autor = dom.find_all(class_='md-datos')[i].p.a.text
        except:
            autor = str('N/A')
        archivo_out.write(titulo + '_' + autor + '_' + precio + '\n')
        
#==========================================================================

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome("./chromedriver",options=op)

driver.get('https://www.cuspide.com/resultados.aspx?c=Biología,%20Ciencias%20de%20la%20Tierra(Técnicos)&tema=2173&por=Tema&orden=fecha&pg=1')
html = driver.execute_script('return document.documentElement.outerHTML')
dom = BS(html , features = 'html.parser')
      
aprieta_boton = '''
        boton = document.querySelector('[class="paginadorLinkSiguiente"]').click()
        '''
existe_boton =  '''
        boton = document.querySelector('[class="paginadorLinkSiguiente"]')
        if (boton){
                return 'Existe'
        } else {
                return 'No existe'
        }
        '''  
   
sleep(3)

#==========================================================================
#======================== GUARDA LIBROS EN CSV ============================
#==========================================================================

archivo_out = open('libros_cuspide.csv','w',encoding = 'utf-8')

#archivo_out = 'Nombre del libro,Autor,Precio\n'
#next(archivo_out)

while driver.execute_script(existe_boton)  != 'No existe':
    guardar_en_csv()        
    driver.execute_script(aprieta_boton)

if driver.execute_script(existe_boton)  == 'No existe':
    guardar_en_csv()      

archivo_out.close()

#==========================================================================
#======================== GUARDA LIBROS EN BASE ===========================
#==========================================================================

archivo_out = open('libros_cuspide.csv')

libros = []

for linea in archivo_out:
    info = linea.split('_')
    libros.append((info[0],info[2],info[1]))

conexion = mysql.connector.connect(
                 host = 'cloud.eant.tech',
                 database = 'pdp_base012',
                 user = 'pdp_usuario012',
                 password = 'eantpass')

cursor = conexion.cursor()
sql = "INSERT INTO `Libros_cuspide`(`titulo`, `precio`, `autor`) VALUES (%s,%s,%s)"
cursor.executemany(sql,libros)

conexion.commit()
cursor.close()
conexion.close()
archivo_out.close()