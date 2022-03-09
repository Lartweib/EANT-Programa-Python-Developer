import requests
import json
import pprint

archivo_in = open('calles_sin_normalizar.csv','r')
archivo_out = open('calles_normalizadas.csv','w')
next(archivo_in)

#archivo_out = 'Dirección Original , Existe? , Calle Normalizada , Número normalizado , Partido Normalizado , Localidad Normalizada , Lat , Lon /n '
#archivo_out(next)               
# No me funcionan estas lineas

for linea in archivo_in:
    #print(linea)
    informacion = linea.split(';')[0]
    #print(informacion)
    
    direccion = informacion.split(',')[0]
    try:
        municipio = informacion.split(',')[1]
    except:
        municipio = ''
    
    direccion_formato = requests.utils.quote(direccion + ', ' +municipio)
    print(direccion_formato)
    
    url = 'http://servicios.usig.buenosaires.gob.ar/normalizar/?geocodificar=True&direccion=' + direccion_formato

    dir_normalizada = json.loads(requests.get(url).text)
    pprint.pprint(dir_normalizada['direccionesNormalizadas'])
    
    if dir_normalizada['direccionesNormalizadas']==[]:
        print('No existe')
        existe = 'No'
        archivo_out.write(direccion + '_' + municipio + '_' + existe + '\n')
    else:
        existe = 'Si'
        calle_normalizada = dir_normalizada['direccionesNormalizadas'][0]['nombre_calle']
        numero_normalizado = dir_normalizada['direccionesNormalizadas'][0]['altura']
        partido_normalizado = dir_normalizada['direccionesNormalizadas'][0]['nombre_partido']
        localidad_normalizada = dir_normalizada['direccionesNormalizadas'][0]['nombre_localidad']
        latitude = dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['x']
        longitude = dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['y']
        archivo_out.write(direccion + '_' + municipio + '_' + existe + '_' + calle_normalizada + \
                      '_' + str(numero_normalizado) + '_' + partido_normalizado + '_' + localidad_normalizada + \
                      '_' + str(latitude) + '_' + str(longitude) + '\n')
            
    print('-----------------')

archivo_out.close()