from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

#estudiante  = {'nombre': 'Eduardo', 'apellido': 'Sanz'}
#Insertar un documento
#cliente.universidad.alumnos.insert_one(estudiante)

bd = cliente['universidad']
coleccion = bd['alumnos']
#Insertar varios documentos a la vez
estudiantes = [{'nombre': 'Ramón', 'apellido': 'Ayala'},
               {'nombre': 'Peter', 'apellido': 'Capusotto'},
               {'nombre': 'Alfredo', 'apellido': 'Nadie',
                'hijos':[{'nombre': 'Jacinto', 'edad': 10},
                         {'nombre': 'Jimena', 'edad': 7}]}
               ]

coleccion.insert_many(estudiantes)
print("Datos Subidos")