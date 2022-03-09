import mysql.connector
conexion = mysql.connector.connect(
                    host = 'cloud.eant.tech',
                    database = 'pdp_base023',
                    user = 'pdp_usuario023',
                    password = 'eantpass')

cursor = conexion.cursor()  

while True:
   control = True
   nombre = input('Ingrese el nombre del alumno (ENTER para salir): ')
   if nombre == '': break
   apellido = input('Ingrese el apellido del alumno: ')
   dni = int(input('Ingrese el dni del alumno: '))
   query = "SELECT dni FROM alumnos"
   cursor.execute(query)
   for dni_bd in cursor:
      if dni_bd[0] == dni:
         print("Este alumno ya está cargado en la base de datos")
         control = False   
   if control:
      mail = input('Ingrese el mail del alumno: ')
      fecha_nac = input('Ingrese la fecha de nacimiento del alumno (AAAA-MM-DD): ')
      sql = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES ('"+ nombre +"' , '"+ apellido +"' ,'"+ str(dni) +"','"+ mail +"' , '"+ fecha_nac +"')"
      cursor.execute(sql)
      
conexion.commit() 
cursor.close()
conexion.close()
print("Datos subidos")