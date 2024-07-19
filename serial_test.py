import serial, time

ser = serial.Serial('/dev/cu.usbmodem101', 9600)
time.sleep(5)

ser.write(str(99).encode())
ser.close()