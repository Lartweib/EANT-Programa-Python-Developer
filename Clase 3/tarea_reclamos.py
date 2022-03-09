import csv
import funciones_normalizacion as norma


archivo_in = 'reclamos.csv'
archivo_out = 'rechamos_normalizado.csv'
     
with open(archivo_in, newline='') as csv_in, open(archivo_out, 'w', newline='', encoding='utf-8') as csv_out:
    csv_reader = csv.reader(csv_in, delimiter = ';', quotechar='"')
    csv_write =  csv.writer(csv_out, delimiter = ';')
    reg_numero = 0
    header = next(csv_reader)
    csv_write.writerow(header)
    for linea in csv_reader:
        fecha_original = linea[3]
        reg_numero +=1
        try: 
            fix_fecha = norma.normalizadorFechas(1,fecha_original,'%d/%m/%y')
        except: 
             try:
                 fix_fecha = norma.normalizadorFechas(2,linea[3],'%Y-%m-%d')    
             except: 
                 try:
                     fix_fecha = norma.normalizadorFechas(3,linea[3],'%Y-%d-%m')
                 except: 
                     try:
                         fix_fecha = norma.normalizadorFechas(4,linea[3],'%d-%m-%Y')
                     except: 
                         try:
                             fix_fecha = norma.normalizadorFechas(5,linea[3],'%d/%m/%Y')
                         except: 
                             try:
                                 fix_fecha = norma.normalizadorFechas(6,norma.traductorFecha(fecha_original),'%d/%m/%Y')
                             except: print('check ',str(reg_numero),linea[3]) #Forma de control si queda alguna fecha con formato incorrecto
                                    
        Lista_fix = (linea[0],linea[1],linea[2],fix_fecha)
        csv_write.writerow(Lista_fix)
        
 
        
    