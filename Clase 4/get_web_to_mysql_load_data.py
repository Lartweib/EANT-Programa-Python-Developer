#import mysql.connector
from datetime import datetime
import csv
import sys
import pymysql
import requests
from io import StringIO


def Link_a_csv(url,archivo_destino):
    respuesta = requests.get(link)
    respuesta.encoding ='utf-8'
    contenido = respuesta.text
    archivo_in = StringIO(contenido)
    csv_temp_in = csv.reader(archivo_in)
    
    data_temp_out = StringIO()
    csv_salida = open(archivo_destino, 'w+')
    csv_writer = csv.writer(data_temp_out, delimiter=',', skipinitialspace=True)
    
    try:
        contador = 0
        next(csv_temp_in)
        for linea in csv_temp_in:
            CsvLinea = []
            for campo in linea:
                CsvLinea.append(campo)    
        
            csv_writer.writerow(CsvLinea)
            data_temp_out.seek(0)
            contador += 1
            resultado = data_temp_out.read()
            
        resultado = resultado.replace('\r', '')
        csv_salida.write(resultado)
    finally:
        archivo_in.close()
        data_temp_out.close()
        csv_salida.close()
    
    return None


def csv_to_mysql(load_sql, host, user, password):
    '''
    This function load a csv file to MySQL table according to
    the load_sql statement.
    '''
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)

        cursor = con.cursor()
        cursor.execute('TRUNCATE TABLE pdp_base009.sa_unidades_febriles;')
        print(datetime.now(),' - Tabla Truncada...')
        
        cursor.execute(load_sql)
        print(datetime.now(), ' - Registros cargados a la tabla desde csv.')
        con.close()
       
    except Exception as pincho:
        print('Error: {}'.format(str(pincho)))
        sys.exit(1)


link = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/ufus/ufus.csv'
archivo_destino = 'temp.csv'
 
host = ''
user = ''
password = ''

print(datetime.now(),' - Inicio')

archivo_csv = Link_a_csv(link,archivo_destino)  
print(datetime.now(),' - csv generado') 

sql_temp = """LOAD DATA LOCAL INFILE \'{archivo}\'  INTO TABLE pdp_base009.sa_unidades_febriles\
    CHARACTER SET latin1\
    FIELDS TERMINATED BY ','\
    ENCLOSED BY '"';"""
    
load_sql = sql_temp.format(archivo=archivo_destino)
    
csv_to_mysql(load_sql, host, user, password)
print(datetime.now(),' - Fin!')  
