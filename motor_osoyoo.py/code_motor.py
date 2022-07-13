import RPi.GPIO as GPIO #control the motor pins through GPIO pins
import time


#if IN1Rear = true and IN2Rear = false -> Move forward
#if IN1rear = false and IN2Rear = True -> Move Reverse
#else stop
IN1Rear = 16 #gpio23-right wheel
IN2Rear = 18 #gpio24-right wheel

#if IN3Rear = true and IN4Rear = false, left motor move forward
#if IN3Rear = false and IN4Rear = true, left motor move reverse
#else stop
IN3Rear = 13 #gpio27-left wheel
IN4Rear = 15 #gpio22-left wheel

#for speed control/PWM of the rear motors through ChangeDutyCycle(speed) function
ENARear = 12 #gpio21 PWM of right motor
ENBRear = 33 #gpio13 PWM of left motor


#if IN1Front = True and IN2Front = False, right motor move forward else
#if IN1Front = false and IN2Front = true, right motor move reverse
IN1Front = 40 #gpio21 front right
IN2Front = 38 #gpio20 front right

#if IN3Front = True and IN4Front = False, left motor move forward else
#if IN4Front = False and IN4Front = true, left motor move reverse
IN3Front = 36 #gpio16 front left
IN4Front = 32 #gpio12 front left

#ENAFront = 
#ENBFront = 
#initialize the GPIO pins and tell the OS the pins that are going to be used to control 
#the pi 3b+ L298N board

GPIO.setmode(GPIO.BOARD) #not the GPIO addressing format

GPIO.setup(IN1Rear, GPIO.OUT) 
GPIO.setup(IN2Rear, GPIO.OUT)
GPIO.setup(IN3Rear, GPIO.OUT)
GPIO.setup(IN4Rear, GPIO.OUT)

GPIO.setup(ENARear, GPIO.OUT)
GPIO.setup(ENBRear, GPIO.OUT)

GPIO.setup(IN1Front, GPIO.OUT) 
GPIO.setup(IN2Front, GPIO.OUT)
GPIO.setup(IN3Front, GPIO.OUT)
GPIO.setup(IN4Front, GPIO.OUT)

GPIO.setup(ENAFront, GPIO.OUT)
GPIO.setup(ENBFront, GPIO.OUT)

GPIO.output(ENAFront,True)
GPIO.output(ENBFront,True)

GPIO.output(ENARear,True)
GPIO.output(ENBRear,True)

#initialize both drivers PWM 
freq_ENARear = GPIO.PWM(ENARear, 100)
freq_ENBRear = GPIO.PWM(ENBRear, 100)

freq_ENARear.start(0)
freq_ENBRear.start(0)

freq_ENAFront = GPIO.PWM(ENAFront, 100)
freq_ENBFront = GPIO.PWM(ENBFront, 100)

freq_ENAFront.start(0)
freq_ENBFront.start(0)

##########REAR RIGHT#####

#make rear right motor moving forward
def rr_ahead(speed):
    GPIO.output(IN1Rear,True)
    GPIO.output(IN2Rear,False)

#make rear right motor moving reverse
def rr_back(speed):
    GPIO.output(IN2Rear,True)
    GPIO.output(IN1Rear,False)

######REAR LEFT###########

#make rear left motor moving forward    
def rl_ahead(speed):  
    GPIO.output(IN3Rear,True)
    GPIO.output(IN4Rear,False)

#make rear left motor moving backward    
def rl_back(speed):  
    GPIO.output(IN4Rear,True)
    GPIO.output(IN3Rear,False)

####FRONT RIGHT#####

#make front right motor moving forward
def fr_ahead(speed):
    GPIO.output(IN1Front,True)
    GPIO.output(IN2Front,False)

#make Front right motor moving backward
def fr_back(speed):
    GPIO.output(IN2Front,True)
    GPIO.output(IN1Front,False)

#########FRONT LEFT ##########

#make Front left motor moving forward    
def fl_ahead(speed):  
    GPIO.output(IN3Front,True)
    GPIO.output(IN4Front,False)

#make Front left motor moving backward    
def fl_back(speed):  
    GPIO.output(IN4Front,True)
    GPIO.output(IN3Front,False)


#############STOP MOTORS##########
#make both motor stop
def stop_car():
    GPIO.output(IN1Rear,False)
    GPIO.output(IN2Rear,False)
    GPIO.output(IN3Rear,False)
    GPIO.output(IN4Rear,False)
    GPIO.output(IN1Front,False)
    GPIO.output(IN2Front,False)
    GPIO.output(IN3Front,False)
    GPIO.output(IN4Front,False)
    
def go_ahead(speed):
    rl_ahead(speed)
    rr_ahead(speed)
    fl_ahead(speed)
    fr_ahead(speed)
    
def go_back(speed):
    rr_back(speed)
    rl_back(speed)
    fr_back(speed)
    fl_back(speed)

#making right turn   
def turn_right(speed):
    rl_ahead(speed)
    rr_back(speed)
    fl_ahead(speed)
    fr_back(speed)
      
#make left turn
def turn_left(speed):
    rr_ahead(speed)
    rl_back(speed)
    fr_ahead(speed)
    fl_back(speed)

# parallel left shift 
def shift_left(speed):
    fr_ahead(speed)
    rr_back(speed)
    rl_ahead(speed)
    fl_back(speed)

# parallel right shift 
def shift_right(speed):
    fr_back(speed)
    rr_ahead(speed)
    rl_back(speed)
    fl_ahead(speed)

def upper_right(speed):
    rr_ahead(speed)
    fl_ahead(speed)

def lower_left(speed):
    rr_back(speed)
    fl_back(speed)
    
def upper_left(speed):
    fr_ahead(speed)
    rl_ahead(speed)

def lower_right(speed):
    fr_back(speed)
    rl_back(speed)