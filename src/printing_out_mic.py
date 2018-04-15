import serial, string, time
#bruh
output = " "

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)

while True:
    print "-----"
    output = ser.readline()
    print output
    output = " "
