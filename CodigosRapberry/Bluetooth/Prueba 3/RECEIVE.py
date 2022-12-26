import bluetooth
from time import sleep

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 5
#bluetooth.get_available_port( bluetooth.RFCOMM )
server_sock.bind(("",port))
server_sock.listen(1)

print("Intentando conectar...")
client_sock,address = server_sock.accept()
print(client_sock,address)
print ("Conexion Aceptada con:",address)

i=0
while True:
  print("Recibiendo...",i)
  data = client_sock.recv(1024)
  print ("received [%s]" % data)
  i=i+1
  sleep(1)


client_sock.close()
server_sock.close()