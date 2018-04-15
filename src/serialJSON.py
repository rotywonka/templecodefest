#!/usr/bin/python
import serial, string, time
import json
from ftplib import FTP

ftp = FTP('https://files.000webhost.com/')
ftp.login(user= 'tuf60598', passwd = 'plokijuh123')
ftp.cwd('/json_filess/')

dict = {}
output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
i = 0.0

while True:
    output = ser.readline()
    dict[j] = {
    'decibel': output
    }
    i = i + 0.00001
    s = json.dumps(dict)
    with open("/Users/ianapplebaum/Desktop/json_files/json.txt", "w") as f:
        f.write(s)

    placefile()


def placefile():

    filename = "/Users/ianapplebaum/Desktop/json_files/json.txt"
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
