import time
from pynput.keyboard import Key, Controller


keyboard = Controller()
key = "a"

time.sleep(5)  # type: ignore
keyboard.press(key)
keyboard.release(key)
print("Escriba algo:")
input()