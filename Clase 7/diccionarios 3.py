import pprint

#Diccionario
perro_a = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'labrador'}
perro_b = {'nombre': 'Picante',
         'tipo': 'perro',
         'raza': 'salchicha'}
perro_c = {'nombre': 'Fatiga',
         'tipo': 'perro',
         'raza': 'n/n'}

#Variable
edad = 5

#Lista
le_gusta_a= ['Comer','Correr a las palomas', 'ladrar sin parar']
le_gusta_b= ['Ladrar','romper el sillon']
le_gusta_c= ['dormir', 'pasear']

#combinar
perro_a.update(edad=edad)
perro_a.update({'le_gusta': le_gusta_a})

pprint.pprint(perro_b)

print(perro.get('le_gusta'))
print(perro.get('le_gusta')[0])

#nuevo objeto amo
amo = {'nombre': 'Javier',
       'tipo': 'humano',
       'edad': 45,
       'le_gusta': ['los fichines','salir los sabados','el futbol'],
       'mascota': perro_a,perro_b,perro_c}

pprint.pprint(amo)