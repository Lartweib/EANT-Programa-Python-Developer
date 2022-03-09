from datetime import datetime
def normalizadorFechas(fecha, formato_in, formato_out = "%d-%m-%Y"):
   objeto_fecha = datetime.strptime(fecha, formato_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, formato_out)
   print(fecha,'->', objeto_fecha, '->', fecha_normalizada)

fecha = "13/2/2019"
normalizadorFechas(fecha, '%d/%m/%Y')

fecha = "2/13/2019"
normalizadorFechas(fecha, '%m/%d/%Y')
# fecha = "02/19" (mes/año)

fecha = "20191302"
normalizadorFechas(fecha, '%Y%d%m')

fecha = "2019-13-02 14:23:33"
normalizadorFechas(fecha, '%Y-%d-%m %H:%M:%S')
# fecha = "13/Feb/2019"
# fecha = "13/February/2019"

fecha = "13 days after February 2019"
normalizadorFechas(fecha, '%d days after %B %Y', '%d/%m/%Y')

meses = ["ENERO","FEBRERO","MARZO",'ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
fecha = "13/Febrero/2019"
lista = fecha.split('/')
mes = lista[1].upper()
nro_mes = meses.index(mes) + 1
fecha_aux = lista[0] + '/' + str(nro_mes) + '/' + lista[2]
normalizadorFechas(fecha_aux, '%d/%m/%Y')