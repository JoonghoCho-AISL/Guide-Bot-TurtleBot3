#!/usr/bin/env python

# import rospy
# from std_msgs.msg import Float64

import time
import RPi.GPIO as GPIO

import Adafruit_DHT as dht

#Definition of pin
Temp_Data = 22

while True:


    humidity, temperature = dht.read_retry(11, Temp_Data)

    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))


GPIO.cleanup()