from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

bd = cliente['universidad']
coleccion = bd['alumnos']

alumnos = coleccion.find()

for alumno in alumnos:
    print(alumno['nombre'])