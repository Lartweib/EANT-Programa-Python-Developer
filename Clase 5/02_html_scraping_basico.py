import requests

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

for lib in range(100):
   if lib < 10: pos = html.find("ctl0" + str(lib) + "_img_tapa")
   else: pos = html.find("ctl" + str(lib) + "_img_tapa")
   segmento = html[pos+58: pos+150]
   pos_final = segmento.find('"')
   nombre_libro = segmento[: pos_final]
   print(lib+1, nombre_libro)