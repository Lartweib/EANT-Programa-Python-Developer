import mysql.connector

conexion = mysql.connector.connect(
                  host = 'cloud.eant.tech',
                  database = 'pdp_base023',
                  user = 'pdp_usuario023',
                  password = 'eantpass')

cursor = conexion.cursor()
sql = '''INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac)
VALUES ("Edgardo", "Tostado", "36852456", "edgardo@nada.com", "2002-5-5")'''

cursor.execute(sql)
conexion.commit()

cursor.close()
conexion.close()