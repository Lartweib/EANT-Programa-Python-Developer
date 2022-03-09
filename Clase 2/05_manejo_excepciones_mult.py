from datetime import datetime

def normalizadorFechas(n, fecha, formato_in, formato_out = "%d-%m-%Y"):
   objeto_fecha = datetime.strptime(fecha, formato_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, formato_out)
   print("Funcionó el método:", n)
   print(fecha,'->', objeto_fecha, '->', fecha_normalizada)

fecha = '10 days'

try:
   normalizadorFechas(1, fecha, '%d days after %Y')
except:
   try:
      normalizadorFechas(2, fecha, '%d days %Y')
   except:
      try:
         normalizadorFechas(3, fecha, '%d days')
      except:
         fecha = 'N/A'
         print(fecha)