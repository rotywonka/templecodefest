
import RPi.GPIO as GPIO
from time import sleep
import serial, string, time
import datetime
from firebase import firebase
#import Adafruit_DHT

import urllib2, urllib, httplib
import json
import os 
from functools import partial

#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
#GPIO.setwarnings(False)

dict = {}
output = " "
ser = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
i = 0.0



# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
#sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = 1,2
# Adafruit_DHT.read_retry(sensor, pin)


firebase = firebase.FirebaseApplication('https://alarm-e979c.firebaseio.com/', None)
#firebase.put("/dht", "/temp", "0.00")
#firebase.put("/dht", "/humidity", "0.00")
data = 'fuck leo'
def update_firebase():
        
    #data = {"Microphone1": }
    while ser.in_waiting:
        output = ser.readline()
        dict = {'decibel': output}
        print(output)
        firebase.post('/sensor/', dict)
#    firebase.post('', dict)	

while True:
		update_firebase()
		
        #sleepTime = int(sleepTime)
		
	








