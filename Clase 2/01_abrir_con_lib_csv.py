import csv
archivo_in = open('peliculas.csv', encoding='utf-8')
tabla = csv.reader(archivo_in, delimiter = ',')

for linea in tabla:
   print(linea[3])