import RPi.GPIO as GPIO
from time import sleep #we only require the delay
GPIO.setmode(GPIO.BCM) #broadcom -> GPIO#
GPIO.setwarnings(False) #disables all warnings

#Create a Class instance for the motor control

class Motor():

    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A

        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B

        #Declare Pin Mode
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)

        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)

        #declare pwm-pin and set the frequency of rotation
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmA.start(0) #set the dutycycle as 0 -> the speed starts at zero 

        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmB.start(0) #set the dutycycle as 0 -> the speed starts at zero        
        
    def moveFoward(self, speed=0.5, turn=0, t=0):#speed and turn are normalized values

        speed *= 100
        turn *= 100
        self.pwmA.ChangeDutyCycle(speed) #user defined else 50
        GPIO.output(self.In1A, GPIO.LOW) #set the directions
        GPIO.output(self.In2A, GPIO.HIGH)

        self.pwmB.ChangeDutyCycle(speed) #user defined else 50
        GPIO.output(self.In1B, GPIO.LOW) #set the directions
        GPIO.output(self.In2B, GPIO.HIGH)
        
        sleep(t) #user defined else 0

    #since speeds cant be same, as forward, we need another genaral speed function
    def move(self, speed=0.5, turn=0, t=0):
        speed *= 100
        turn *= 100

        #to invtoduce a variableness in turn, 
        leftSpeed = speed #50-20
        rightSpeed = speed# 50 + 20 right speed is higher, move to the right

        #to limit values btn the required threshold
        if leftSpeed > 100: leftSpeed =100
        elif leftSpeed < -100: leftSpeed= -100
        if rightSpeed > 100: rightSpeed =100
        elif rightSpeed < -100: rightSpeed= -100

        #duty cycle doesn't take negative values -
        #  change in rotation happens when polarity is reversed
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed>0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else: 
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        if rightSpeed>0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)

        sleep(t)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)        
        self.pwmB.ChangeDutyCycle(0)
        sleep(t)



def main():
    motor1.move(0.6, 0, 2)
    motor1.stop(0.1)

#create a motor2 - driver - instance
# e.g motor2 = Motor(2,3,4,17, 22, 27)

#if this module is to be called...

if __name__ == '__main__': #checks whether this module is running as main
    #if this is true, we run the main function
    #the motor follow these sequences of rotation
    #create a motor1 - driver -  instance
    #motor1 = Motor(3,5,7, 11, 13, 15)
    motor1 = Motor(2,3,4,17, 27, 22)
    main()