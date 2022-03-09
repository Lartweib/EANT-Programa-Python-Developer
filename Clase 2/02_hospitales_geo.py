import csv
archivo_in = open('hospitales.csv','r',encoding = 'utf-8')
archivo_out = open('hospitales_mod.csv','w',encoding = 'utf-8')
lectura = csv.reader(archivo_in)
next(lectura)
archivo_out.write("latitude,longitude,name,label\n")
for lista in lectura:
    #print(lista[1], lista[0], lista[4], lista[8])
    archivo_out.write(lista[1] + ',' + lista[0] + ',' + lista[8] + ',' + lista[4] + '\n')
archivo_in.close()
archivo_out.close() 
