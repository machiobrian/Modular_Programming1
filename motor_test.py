#have a module for speed and direction

import RPi.GPIO as GPIO
from time import sleep #we only require the delay
GPIO.setmode(GPIO.BCM) #broadcom
GPIO.setwarnings(False) #disables all warnings

Ena = 2 #enable pin controls the speed 
In1 = 3 #Input pins contorl the direction
In2 = 4

#Declare Pin Mode
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

#declare pwm-pin and set the frequency of rotation
pwmA = GPIO.PWM(Ena, 100)
pwmA.start(0) #set the dutycycle as 0 -> the speed starts at zero

pwmA.ChangeDutyCycle(60) #initiate the speed as 60% of the duty cycle
GPIO.output(In1, GPIO.LOW) #set the directions
GPIO.output(In2, GPIO.HIGH)
sleep(2) #delay the state for the next two seconds
pwmA.ChangeDutyCycle(0) #speed set to null
