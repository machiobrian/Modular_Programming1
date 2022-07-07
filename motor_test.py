#have a module for speed and direction

import RPi.GPIO as GPIO
from time import sleep #we only require the delay
GPIO.setmode(GPIO.BCM) #broadcom
GPIO.setwarnings(False) #disables all warnings

Ena = 2 #enable pin controls the speed 
In1a = 3 #Input pins contorl the direction
In2a = 4

Enb = 17
In1b = 27
In2b = 22

#Declare Pin Mode
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1a, GPIO.OUT)
GPIO.setup(In2a, GPIO.OUT)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In1b, GPIO.OUT)
GPIO.setup(In2b, GPIO.OUT)


######MOTOR 2A
#declare pwm-pin and set the frequency of rotation
pwmA = GPIO.PWM(Ena, 100)
pwmA.start(0) #set the dutycycle as 0 -> the speed starts at zero



pwmA.ChangeDutyCycle(60) #initiate the speed as 60% of the duty cycle
GPIO.output(In1a, GPIO.LOW) #set the directions
GPIO.output(In2a, GPIO.HIGH)
sleep(2) #delay the state for the next two seconds
pwmA.ChangeDutyCycle(0) #speed set to null

sleep(2) #delay for a reverse spin

pwmA.ChangeDutyCycle(60)
GPIO.output(In1a, GPIO.HIGH) #set the directions
GPIO.output(In2a, GPIO.LOW)
sleep(2) #delay the state for the next two seconds
pwmA.ChangeDutyCycle(0)

######MOTOR 2B

pwmB = GPIO.PWM(Enb, 100)
pwmB.start(0)

pwmB.ChangeDutyCycle(60) #initiate the speed as 60% of the duty cycle
GPIO.output(In1b, GPIO.LOW) #set the directions
GPIO.output(In2b, GPIO.HIGH)
sleep(2) #delay the state for the next two seconds
pwmB.ChangeDutyCycle(0) #speed set to null

sleep(2)

pwmB.ChangeDutyCycle(60)
GPIO.output(In1b, GPIO.HIGH) #set the directions
GPIO.output(In2b, GPIO.LOW)
sleep(2) #delay the state for the next two seconds
pwmB.ChangeDutyCycle(0)

