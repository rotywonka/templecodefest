#!/usr/bin/python
import serial, string, time

def readSer():
    dict = {}
    output = " "
    ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
    i = 0.0
    
    output = ser.readline()
    dict[i] = {
        'decibel': output
    }
        
    i = i + 0.00001
    return dict
