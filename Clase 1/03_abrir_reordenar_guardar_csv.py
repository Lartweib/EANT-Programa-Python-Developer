#Abro y trabajo un CSV

archivo_in = open('archivos/subtes.csv', encoding = 'utf-8')
archivo_out = open('archivos/subtes_mod.csv', 'w', encoding = 'utf-8')
for linea in archivo_in:
   linea = linea.replace('\n','')
   lista = linea.split(',')
   #print(lista[2], lista[1], lista[0])
   archivo_out.write(lista[2] + ',' + lista[1] + ',' + lista[0] + '\n')
archivo_in.close()
archivo_out.close()