import mysql.connector

miBD = mysql.connector.connect(
  host = "remotemysql.com",
  user = "98EjZpC5Ln",
  password = "7Q7Hxi197V",
  database = "98EjZpC5Ln"
)

print(miBD)

mySQLcursor = miBD.cursor()

# Mostrar todas las tablas
mySQLcursor.execute("SHOW TABLES")
for x in mySQLcursor:
  print(x)

# Realizar una consulta
mySQLcursor.execute("SELECT * FROM jedis")
resultado = mySQLcursor.fetchall()
# Imprimir todas las columnas
for x in resultado:
  print(x)
  
# Imprimir solo una columna
for x in resultado:
  print(x[1])


