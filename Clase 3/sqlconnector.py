import mysql.connector

conexion = mysql.connector.connect(
            host = '',
            database = '',
            user = '',
            password = '')

cursor = conexion.cursor()
sql = 'SELECT * FROM alumnos'

cursor.execute(sql)

for alumno in cursor:
    print(alumno)
    
cursor.close()
conexion.close()

