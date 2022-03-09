import requests
import csv
from io import StringIO
from datetime import datetime
import mysql.connector


conexion = mysql.connector.connect(
                                    host = 'cloud.eant.tech',
                                    database = '',
                                    user= '',
                                    password= ''
                                    )

cursor = conexion.cursor()


cursor.execute('TRUNCATE TABLE pdp_base009.sa_unidades_febriles;')
print(datetime.now(),' - Tabla Truncada...')

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/ufus/ufus.csv'

respuesta = requests.get(url)
respuesta.encoding ='utf-8'
contenido = respuesta.text
archivo = StringIO(contenido)

print(datetime.now(),' - Comienzo insert de registros...')

objeto_csv = csv.reader(archivo)
header = next(objeto_csv)
encabezado = list(map(lambda x:x.lower(),header))
reg_numero = 0
for linea in objeto_csv:
    reg_numero +=1
    var_string = ['%s'] * len(linea)
    sql_template = """
    INSERT INTO sa_unidades_febriles ({columns}) VALUES ({var_string})
    """
    sql =  sql_template.format(
                                columns=','.join(encabezado),
                                var_string=','.join(var_string)
                                )

    cursor.execute(sql, linea)
            
conexion.commit()

print('Registros leidos: ',str(reg_numero))
cursor.execute('select count(*) from sa_unidades_febriles;')
print('registros insertados: ',cursor.fetchone())


archivo.close()
cursor.close()
conexion.close()

print(datetime.now(),' - Fin!') 
