

import requests 
import json 
import pprint 
from selenium import webdriver


# print(direccion +' ' + altura +',' + localidad)


# driver.get("https://www.google.com/maps/search/34%C2%B036'11.3%22S+58%C2%B022'15.2%22W/@-34.6031378,-58.3714374,19z")
respuesta = True

def normalizar(objeto):
    try:
        if(objeto['errorMessage']):
            print(objeto['errorMessage'])
    except :        
        for i in range(len(objeto['direccionesNormalizadas'])):   
            altura = objeto['direccionesNormalizadas'][i]['altura']
            nombre_calle_cruce = objeto['direccionesNormalizadas'][i]['nombre_calle_cruce']
            localidad = objeto['direccionesNormalizadas'][i]['nombre_localidad']
            codigo_calle = objeto['direccionesNormalizadas'][i]['cod_calle']
            direccion = objeto['direccionesNormalizadas'][i]['direccion']
            latitud = objeto['direccionesNormalizadas'][i]['coordenadas']['x']
            longitud = objeto['direccionesNormalizadas'][i]['coordenadas']['y']
            print(direccion,altura,nombre_calle_cruce,localidad,codigo_calle,latitud,longitud)
            coordenadas_formato = requests.utils.quote(longitud+latitud)
            driver = webdriver.Chrome(executable_path='C:/Users/crist/OneDrive/Documentos/curso_data_developer/clase_6/chromedriver.exe')
            driver.get("https://www.google.com/maps/search/" +coordenadas_formato)

while respuesta:
    direccion =input('ingrese la direccion: ')
    altura = input('ingrese la altura: ')
    localidad = 'caba'
    direccion_formato = requests.utils.quote(direccion +' '+ altura + ',' + localidad)
    url = 'http://servicios.usig.buenosaires.gob.ar\
/normalizar/?geocodificar=True&direccion=' +direccion_formato
    obj = json.loads(requests.get(url).text)
    resp = input('Ingresar otra direccion? s/n: ').upper()
   
    # pprint.pprint(objeto)
    normalizar(obj)
    
    if(resp == 'N'):
        respuesta = False
# driver.quit()










    
    

