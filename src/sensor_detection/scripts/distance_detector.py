#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

import time
import RPi.GPIO as GPIO

#Definition of pins
EchoPin = 3
TrigPin = 2

#Set GPIO 
#Ultrasonic pin initialization
def GPIO_Init():
    #set the GPIO port to BCM encoding mode.
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)

    #Set Ultrasocin pin
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)

#Distance measurement
def distance_measurement():
    #output Low
    GPIO.output(TrigPin,GPIO.LOW)
    time.sleep(0.000002)
    #output High
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    #output Low
    GPIO.output(TrigPin,GPIO.LOW)

    t3 = time.time()
    #too long distance -> -1
    while not GPIO.input(EchoPin):
        t4 = time.time()        
        if (t4 - t3) > 0.03 :
            return -1

    #Incorrect signal
    t1 = time.time()
    while GPIO.input(EchoPin):
        t5 = time.time()
        if(t5 - t1) > 0.03 :
            return -1

    t2 = time.time()
    time.sleep(0.01)
    #print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    return ((t2 - t1)* 340 / 2) * 100

#Publisher of ROS
def publisher():
    #topic = Distance
    pub = rospy.Publisher('Distance',Float64,queue_size=10)
    #node's name = Dist_Publisher
    rospy.init_node('Dist_Publisher')
    #refresh frequench
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        dist = distance_measurement()
        #write log
        rospy.loginfo(dist)
        #publish
        pub.publish(dist)
        rate.sleep()

if __name__=='__main__':
    try:
        GPIO_Init()
        publisher()

    except rospy.ROSInterruptException:
        pass

        


