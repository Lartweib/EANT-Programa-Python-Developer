#Abrir y trabajar un archivo de texto

archivo = open('frutas.txt', 'r', encoding= 'utf-8')
for linea in archivo:
   linea = linea.replace('\n', '')
   print(linea)

archivo.close()
