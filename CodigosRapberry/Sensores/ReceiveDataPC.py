import bluetooth
from time import sleep
from pyautogui import *

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 5
server_sock.bind(("",port))
server_sock.listen(1)

print("Intentando conectar...")
client_sock,address = server_sock.accept()
print(client_sock,address)
print ("Conexion Aceptada con:",address)



distances={}
while True:
  distances[0]=int.from_bytes(client_sock.recv(1024),"big")
  Y1=distances[0]
  distances[1]=int.from_bytes(client_sock.recv(1024),"big")
  Y2=distances[1]
  distances[2]=int.from_bytes(client_sock.recv(1024),"big")
  X3=distances[2]
  distances[3]=int.from_bytes(client_sock.recv(1024),"big")
  X4=distances[3]
  distances[4]=int.from_bytes(client_sock.recv(1024),"big")
  X2=distances[4]
  distances[5]=int.from_bytes(client_sock.recv(1024),"big")
  X1=distances[5]
  
  
  print("Y1: ",Y1,"Y2: ",Y2,"X1: ",X2,"X3: ",X3,"X4: ",X4)
  sleep(1)
  
  
  