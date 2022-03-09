import csv
import requests
import json


#Funcion para obtener json de las direcciones
def ReciveDireccion (in_direccion, in_localidad):
    
    if in_localidad != None:
        direccion_formato = requests.utils.quote(in_direccion+','+in_localidad)
    else:
        direccion_formato = requests.utils.quote(in_direccion)
        

    url = 'https://servicios.usig.buenosaires.gob.ar\
/normalizar/?geocodificar=True&direccion='+direccion_formato

    direccion_json = json.loads(requests.get(url).text)
    
    return  direccion_json


archivo_in = 'calles_sin_normalizar.csv'
archivo_out = 'calles_normalizadas.csv'

#abrir archivo de lectura y escritura     
with open(archivo_in, newline='') as csv_in, open(archivo_out, 'w', newline='') as csv_out:
    csv_reader = csv.reader(csv_in, delimiter = ';')
    csv_write =  csv.writer(csv_out, delimiter = ';')
    header = next(csv_reader)
    csv_write.writerow(header)
    #lectura de registros
    for registro in csv_reader:
        Direccion_Original = registro[0]
        Solo_direccion = Direccion_Original.split(',')[0].upper()
        try:
            Solo_Localidad = Direccion_Original.split(',')[1].upper()
        except:
            Solo_Localidad = None
        #ejecucion de funcion
        direccion_nomalizada = ReciveDireccion(Solo_direccion, Solo_Localidad)
         
        #validacion para direcciones no existentes        
        if len(direccion_nomalizada['direccionesNormalizadas']) != 0:
            
            #cargar direcciones con o sin localidad
            for direccion in range(len(direccion_nomalizada['direccionesNormalizadas'])):
                calle = direccion_nomalizada['direccionesNormalizadas'][direccion]['nombre_calle']
                Numero = direccion_nomalizada['direccionesNormalizadas'][direccion]['altura']
                Partido = direccion_nomalizada['direccionesNormalizadas'][direccion]['nombre_partido']
                Localidad = direccion_nomalizada['direccionesNormalizadas'][direccion]['nombre_localidad']
                coordenadas = direccion_nomalizada['direccionesNormalizadas'][direccion]['coordenadas']    
                Lat = float(coordenadas.get('x'))
                Lon = float(coordenadas.get('y'))
                existe = 'Si'
                direccion_fix = (Direccion_Original,existe,calle,Numero,Partido,Localidad,Lat,Lon)
                csv_write.writerow(direccion_fix)
                
        else: 
            existe = 'No'
            calle = ''
            Numero = ''
            Partido = ''
            Localidad = ''
            Lat = ''
            Lon = ''                                     
            direccion_fix = (Direccion_Original,existe,calle,Numero,Partido,Localidad,Lat,Lon)
            csv_write.writerow(direccion_fix)
            