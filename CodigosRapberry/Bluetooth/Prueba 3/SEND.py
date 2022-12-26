import bluetooth
from time import sleep

bd_addr = "70:66:55:6A:39:A4"

port = 5
#bluetooth.get_available_port( bluetooth.RFCOMM )

print("Intentando conectar...")
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print("CONECTADO con:", bd_addr)

i=0
while True:
  print("Enviando...",i)
  sock.send("MAMADAS")
  i=i+1
  

sock.close()


