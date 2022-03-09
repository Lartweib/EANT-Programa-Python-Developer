import pprint

#Diccionario
perro = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'labrador'}

#Variable
edad = 5

#Lista
le_gusta = ['Comer', 'Correr a las palomas', 'ladrar sin parar']

#Combinar
perro.update(edad = edad)
perro.update({'le_gusta': le_gusta})

pprint.pprint(perro)

print(perro.get('le_gusta')[0])

#Nuevo objeto amo
amo = {'nombre': 'Javier',
       'tipo': 'humano',
       'edad': 45,
       'le_gusta': ['los fichines', 'salir los sábados', 'el fútbol'],
       'mascota': perro}

pprint.pprint(amo)