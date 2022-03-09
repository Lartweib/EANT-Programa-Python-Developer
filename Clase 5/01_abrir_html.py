import pprint

html = open('pagina_web.html', encoding='utf-8')
for linea in html:
   pprint.pprint(linea)