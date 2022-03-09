from datetime import datetime

fecha = "10 days 2021"

try:
   objeto_fecha = datetime.strptime(fecha, '%d days after %Y')
   fecha_normalizada = datetime.strftime(objeto_fecha, '%d/%m/%Y')
   print("Funcionó el método 1")
   print(fecha,'->', objeto_fecha, '->', fecha_normalizada)

except ValueError:
   objeto_fecha = datetime.strptime(fecha, '%d days %Y')
   fecha_normalizada = datetime.strftime(objeto_fecha, '%d/%m/%Y')
   print("Funcionó el método 2")
   print(fecha,'->', objeto_fecha, '->', fecha_normalizada)