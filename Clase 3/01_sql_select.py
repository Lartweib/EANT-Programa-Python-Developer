import mysql.connector

conexion = mysql.connector.connect(
                    host = 'cloud.eant.tech',
                  database = '',
                  user = '',
                  password = 'eantpass')

cursor = conexion.cursor()
sql = "SELECT nombre, apellido FROM alumnos where apellido like 'r%'"

cursor.execute(sql)

for alumno in cursor:
   print(alumno)
   
cursor.close()
conexion.close()
