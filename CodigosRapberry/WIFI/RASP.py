from grovepi import *
from time import sleep
import requests

ultrasonic_ranger_1 = 4
ultrasonic_ranger_2 = 3
ultrasonic_ranger_3 = 7
ultrasonic_ranger_4 = 2
ultrasonic_ranger_5 = 5
ultrasonic_ranger_6 = 6

Relay_pin = 2
pinMode(Relay_pin,"OUTPUT")

def EXECUTE(data):
        
        r = requests.post("http://192.168.1.84:5001/EXECUTE", data=data)
def check(X):
    if(X>=256):
        return 255
    else:
        return X
        

if __name__ == '__main__':
    
    while True:
            
            distanceY1 = check(ultrasonicRead(ultrasonic_ranger_1))
            distanceY2 = check(ultrasonicRead(ultrasonic_ranger_2))
            distanceX1 = check(ultrasonicRead(ultrasonic_ranger_3))
            distanceX2 = check(ultrasonicRead(ultrasonic_ranger_4))
            distanceX3 = check(ultrasonicRead(ultrasonic_ranger_5))
            distanceX4 = check(ultrasonicRead(ultrasonic_ranger_6))
            
            print("Y1: ",distanceY1,"Y2: ",distanceY2,"X1: ",distanceX1,"X2: ", distanceX2,"X3: ",distanceX3,"X4: ",distanceX4)
            data=[distanceY1,distanceY2,distanceX1,distanceX2,distanceX3,distanceX4]
            EXECUTE(bytearray(data))
            digitalWrite(Relay_pin,1)
            sleep(0.1)
            

    

    