import pprint
import json

#Diccionario
perro = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'labrador'}

#Variable
edad = 5

#Lista
le_gusta= ['Comer','Correr a las palomas', 'ladrar sin parar']

#combinar
perro.update(edad=edad)
perro.update({'le_gusta': le_gusta})

#pprint.pprint(perro)

objeto = {'perro': perro}

with open('perro.json', 'w', encoding='utf-8') as archivoJson:
    json.dump(objeto, archivoJson)
    
with open('perro_lindo.json', 'w', encoding='utf8') as archivoJson:
    json.dump(objeto, archivoJson)
    