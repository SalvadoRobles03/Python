import mysql.connector

miBD = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "DisneyPlus"
)

print(miBD)

mySQLcursor = miBD.cursor()

# Mostrar todas las tablas
mySQLcursor.execute("SHOW TABLES")
for x in mySQLcursor:
  print(x)

# Realizar una consulta
#mySQLcursor.execute("INSERT INTO jedis (nombre_jedi) values ('Ashoka')")
#miBD.commit()
mySQLcursor.execute("SELECT * FROM pelicula_serie")
resultado = mySQLcursor.fetchall()
# Imprimir todas las columnas
for x in resultado:
  print(x)
  
# Imprimir solo una columna
for x in resultado:
  print(x[1])


