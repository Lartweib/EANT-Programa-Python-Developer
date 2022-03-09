import requests
from io import StringIO
import csv
import mysql.connector

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/oferta-gastronomica/oferta_gastronomica.csv'
bajada = requests.get(url).text
csv = csv.reader(StringIO(bajada))
next(csv)
bares = []

for linea in csv:
   bares.append((linea[1], linea[0], linea[3], linea[13], linea[15][7:]))

conexion = mysql.connector.connect(
                    host = 'cloud.eant.tech',
                    database = 'pdp_base023',
                    user = 'pdp_usuario023',
                    password = 'eantpass')

cursor = conexion.cursor()
cursor.execute("TRUNCATE TABLE bares")
sql = "INSERT INTO bares(latitud, longitud, nombre, direccion, comuna) VALUES(%s,%s,%s,%s,%s)"
cursor.executemany(sql, bares)

conexion.commit()
conexion.close()
