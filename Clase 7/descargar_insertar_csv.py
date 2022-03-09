import requests
from io import StringIO
import csv
import mysql.connector
from datetime import datetime

def get_time():
   ahora = datetime.now()
   hora = ahora.strftime("%H:%M:%S")
   return hora

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/oferta-gastronomica/oferta_gastronomica.csv'
bajada = requests.get(url).text
csv = csv.reader(StringIO(bajada))
next(csv)
conexion = mysql.connector.connect(
                    host = 'cloud.eant.tech',
                    database = 'pdp_base023',
                    user = 'pdp_usuario023',
                    password = 'eantpass')
cursor = conexion.cursor()
cursor.execute("TRUNCATE TABLE bares")
contador = 0
print("Hora de comienzo:", get_time())
for linea in csv:
   sql = "INSERT INTO bares(latitud, longitud, nombre, direccion, comuna) VALUES(%s,%s,%s,%s,%s)"
   cursor.execute(sql, (linea[1], linea[0], linea[3], linea[13], linea[15][7:]))
   contador += 1
   print(contador, "Valor cargado")

print("Hora de finalización:", get_time())
conexion.commit()
conexion.close()
