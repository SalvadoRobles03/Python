from grovepi import *
import bluetooth
from time import sleep

ultrasonic_ranger = 3
ultrasonic_ranger_2 = 2
ultrasonic_ranger_3 = 7
ultrasonic_ranger_4 = 8
Relay_pin = 2
pinMode(Relay_pin,"OUTPUT")
bd_addr = "70:66:55:6A:39:A4"
port = 5


print("Intentando conectar...")
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print("CONECTADO con:", bd_addr)

distances={}

while True:
        
        distanceX1 = ultrasonicRead(ultrasonic_ranger)
        distances[0]=distanceX1
        distanceX2 = ultrasonicRead(ultrasonic_ranger_2)
        distances[1]=distanceX2
        distanceY1 = ultrasonicRead(ultrasonic_ranger_3)
        distances[2]=distanceY1
        distanceY2 = ultrasonicRead(ultrasonic_ranger_4)
        distances[3]=distanceY2
        
        print(distances[0],'cm   ',distances[1], 'cm   ',distances[2],'cm   ',distances[3], 'cm')
        sock.send(distances)
        
        if distanceX1 or distanceX2 or distanceY1 or distanceY2 <= 0:
            digitalWrite(Relay_pin,1)
        else:
            digitalWrite(Relay_pin,0)

  

