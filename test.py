import serial

s = serial.Serial("COM10")
s.baudrate=9600

strData = "123"

encoded = (strData + "\n").encode()
print(encoded)
s.write(encoded)