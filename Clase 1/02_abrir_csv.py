#Abro y trabajo un CSV

archivo = open('archivos/subtes.csv', encoding = 'utf-8')
for linea in archivo:
   linea = linea.replace('\n','')
   lista = linea.split(',')
   print(lista[2])


archivo.close()