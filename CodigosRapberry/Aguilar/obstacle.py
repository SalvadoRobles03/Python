import RPi.GPIO as GPIO
import time
import signal
import sys

def signal_handler(sig, frame):
    GPIO.cleanup()
    print("CTRL+C presionado")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

sensor01 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor01, GPIO.IN)

while True:
    if GPIO.input(sensor01) == False:
        print("Obstaculo detectado")
        time.sleep(1)
