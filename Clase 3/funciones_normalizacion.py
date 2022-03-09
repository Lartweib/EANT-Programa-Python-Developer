from datetime import datetime


def normalizadorFechas(n, fecha, formato_in, formato_out = '%Y-%m-%d'):
    objeto_fecha = datetime.strptime(fecha,formato_in)
    fecha_normalizada = datetime.strftime(objeto_fecha,formato_out)
    return fecha_normalizada

def traductorFecha(fecha_original):
   lista = fecha_original.split(' de ')
   mes = lista[1].upper()
   meses = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
   nro_mes = meses.index(mes)+1
   fecha_aux = lista[0] + '/' + str(nro_mes) + '/' +  lista[2]
   return fecha_aux