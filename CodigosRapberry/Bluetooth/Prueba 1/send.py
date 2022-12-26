import serial

#rfcomm bind 0 D5:C5:D3:52:13:1E

DEVICE = '/dev/rfcomm0'
BAUD_RATE = 9600

# Connect to the device
s = serial.Serial(DEVICE, BAUD_RATE)
print('Connect to', DEVICE)

# Send data
s.write(b'hello\n')