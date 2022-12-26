import serial
from time import sleep


ser = serial.Serial('COM5', 9600)
print(ser.readable)
print("connected to:",ser.portstr)


while True:
    print("reading")
    print(str(ser.readline()))
    sleep(2)
