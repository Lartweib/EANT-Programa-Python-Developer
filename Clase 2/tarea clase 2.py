import csv
from datetime import datetime

def normalizadorFechas(fecha, formato_in, formato_out = "%d-%m-%Y"):
    objeto_fecha = datetime.strptime(fecha, formato_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, formato_out)
    archivo_out.write(linea[0]+ ';'+ linea[1]+ ';'+ linea[2]+ ';'+ fecha_normalizada+ '\n')


    
archivo_in = open('reclamos.csv', encoding = 'ansi')
archivo_out = open('reclamos_normalizado.csv','w',encoding = 'ansi')
reclamos = csv.reader(archivo_in, delimiter = ';')

next(reclamos)
archivo_out.write('id_cliente;tx_zona;tx_reclamo;fc_reclamo\n')
#print('id_cliente;tx_zona;tx_reclamo;fc_reclamo\n')


    


archivo_in.close()
archivo_out.close()