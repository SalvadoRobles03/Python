import RPi.GPIO as GPIO
import time
import signal
import sys

def signal_handler(sig, frame):
    GPIO.cleanup()
    print("CTRL+C presionado")
    sys.exit(0)

def obstaculo_callback(channel):
    print("Obstaculo detectado!")

sensor01 = 14
    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor01, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sensor01, GPIO.FALLING, callback=obstaculo_callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

