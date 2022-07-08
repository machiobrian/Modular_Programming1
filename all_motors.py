import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) #broadcom gpio#
GPIO.setwarnings(False)

#create a class instance for all the motor drivers

class Motor():
    
    def __init__(self, EN1A, IN1A, IN2A, IN3A, IN4A, EN2A,
                       EN1B, IN1B, IN2B, IN3B, IN4B, EN2B ):
                       #A -> Front Motor, B-> Back Motors
        #front
        self.EN1A = EN1A
        self.IN1A = IN1A
        self.IN2A = IN2A
        self.IN3A = IN3A
        self.IN4A = IN4A
        self.EN2A = EN2A

        #back
        self.EN1B = EN1B
        self.IN1B = IN1B
        self.IN2B = IN2B
        self.IN3B = IN3B
        self.IN4B = IN4B
        self.EN2B = EN2B

        #Declare the Pin Modes -> All of them are outputs
        GPIO.setup(self.EN1A,GPIO.OUT)
        GPIO.setup(self.IN1A,GPIO.OUT)
        GPIO.setup(self.IN2A,GPIO.OUT)
        GPIO.setup(self.IN3A,GPIO.OUT)
        GPIO.setup(self.IN4A,GPIO.OUT)
        GPIO.setup(self.EN2A,GPIO.OUT)

        GPIO.setup(self.EN1B ,GPIO.OUT)
        GPIO.setup(self.IN1B,GPIO.OUT)
        GPIO.setup(self.IN2B ,GPIO.OUT)
        GPIO.setup(self.IN3B ,GPIO.OUT)
        GPIO.setup(self.IN4B ,GPIO.OUT)
        GPIO.setup(self.EN2B ,GPIO.OUT)

        #Declare the PWM pins and set the frequency of rotation
        # PWM1A = GPIO.PWM(EN1A, 100)
        # PWM1A.start(0)
        # PWM2A = GPIO.PWM(EN2A, 100)
        # PWM2A.start(0)
        # PWM1B = GPIO.PWM(EN1B, 100)
        # PWM1B.start(0)
        # PWM2B = GPIO.PWM(EN2B, 100)
        # PWM2B.start(0)
        #motor driver A - front
        self.PWM1A = GPIO.PWM(self.EN1A, 60)
        self.PWM1A.start(0.0)
        self.PWM2A = GPIO.PWM(self.EN2A, 60)
        self.PWM2A.start(0.0)

        #motor driver B - back
        self.PWM1B = GPIO.PWM(self.EN1B, 60)
        self.PWM1B.start(0.0)
        self.PWM2B = GPIO.PWM(self.EN2B, 60)
        self.PWM2B.start(0.0)

    def Forward(self, speed=0, t =0):
        #spin all with the same frequency

        #the speed -> frequency of rotation
        #introduce a condition to have the limit to 100 -> frequency limit
        if speed > 100: speed = 100
        elif speed < -100: speed = -100 #remember the PWM does not take negative values

        #therefore we pass absolute values to all pwm pins

        if speed > 0: #to  spin all the motors forward
            self.PWM1A.ChangeDutyCycle(abs(speed))
            GPIO.output(self.IN1A, GPIO.LOW) #front RIGHT
            GPIO.output(self.IN2A, GPIO.HIGH)

            self.PWM2A.ChangeDutyCycle(abs(speed))
            GPIO.output(self.IN3A, GPIO.HIGH) #front LEFT
            GPIO.output(self.IN4A, GPIO.LOW)

            self.PWM1B.ChangeDutyCycle(abs(speed))
            GPIO.output(self.IN1B, GPIO.LOW) #back right
            GPIO.output(self.IN2B, GPIO.HIGH)

            self.PWM2B.ChangeDutyCycle(abs(speed))
            GPIO.output(self.IN3B, GPIO.LOW) #back left
            GPIO.output(self.IN4B, GPIO.HIGH)

        # else: #to  spin all the motors reverse
        #     self.PWM1A.ChangeDutyCycle(abs(speed))
        #     GPIO.output(self.IN1A, GPIO.LOW) #front right
        #     GPIO.output(self.IN2A, GPIO.HIGH)

        #     self.PWM2A.ChangeDutyCycle(abs(speed))
        #     GPIO.output(self.IN3A, GPIO.LOW) #front left
        #     GPIO.output(self.IN4A, GPIO.HIGH)

        #     self.PWM1B.ChangeDutyCycle(abs(speed))
        #     GPIO.output(self.IN1B, GPIO.LOW) #back right
        #     GPIO.output(self.IN2B, GPIO.HIGH)

        #     self.PWM2B.ChangeDutyCycle(abs(speed))
        #     GPIO.output(self.IN3B, GPIO.LOW) #back left
        #     GPIO.output(self.IN4B, GPIO.HIGH)

        sleep(t)

    def stop(self, t=0): #stop wheel rotation
        #Zero all the duty cycles to turn motors off
        self.PWM1A.ChangeDutyCycle(abs(0)) #front left
        self.PWM2A.ChangeDutyCycle(abs(0)) #front right
        

         
        self.PWM1B.ChangeDutyCycle(abs(0)) #back right
        self.PWM2B.ChangeDutyCycle(abs(0)) #back left
        
        sleep(t)
    
    def moveRight(self, speed=0, t =0): #right key
        #1. activate pwm
        #2. set the required pins to HIGH and LOW
        self.PWM1A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1A, GPIO.LOW) #front RIGHT
        GPIO.output(self.IN2A, GPIO.HIGH)

        self.PWM2A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3A, GPIO.LOW) #front LEFT
        GPIO.output(self.IN4A, GPIO.HIGH)

        self.PWM1B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1B, GPIO.HIGH) #back right
        GPIO.output(self.IN2B, GPIO.LOW)

        self.PWM2B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3B, GPIO.LOW) #back left
        GPIO.output(self.IN4B, GPIO.HIGH)


    def moveLeft(self, speed=0, t=0): #left key
        #1. activate pwm
        #2. set the required pins to HIGH and LOW
        self.PWM1A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1A, GPIO.HIGH) #front RIGHT
        GPIO.output(self.IN2A, GPIO.LOW)

        self.PWM2A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3A, GPIO.LOW) #front LEFT
        GPIO.output(self.IN4A, GPIO.HIGH)

        self.PWM1B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1B, GPIO.HIGH) #back right
        GPIO.output(self.IN2B, GPIO.LOW)

        self.PWM2B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3B, GPIO.HIGH) #back left
        GPIO.output(self.IN4B, GPIO.LOW)

    def rotate_135ccw(self, speed=0, t=0): #letter j
        #1. activate pwm
        #2. set the required pins to HIGH and LOW
        self.PWM1A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1A, GPIO.HIGH) #front RIGHT
        GPIO.output(self.IN2A, GPIO.LOW)

        self.PWM2A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3A, GPIO.LOW) #front LEFT
        GPIO.output(self.IN4A, GPIO.HIGH)

        self.PWM1B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1B, GPIO.HIGH) #back right
        GPIO.output(self.IN2B, GPIO.LOW)

        self.PWM2B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3B, GPIO.HIGH) #back left
        GPIO.output(self.IN4B, GPIO.LOW)

    def rotate_90cw(self, speed=0, t=0): #letter k
        #1. activate pwm
        #2. set the required pins to HIGH and LOW
        self.PWM1A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1A, GPIO.HIGH) #front RIGHT
        GPIO.output(self.IN2A, GPIO.LOW)

        self.PWM2A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3A, GPIO.LOW) #front LEFT
        GPIO.output(self.IN4A, GPIO.HIGH)

        self.PWM1B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1B, GPIO.HIGH) #back right
        GPIO.output(self.IN2B, GPIO.LOW)

        self.PWM2B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3B, GPIO.HIGH) #back left
        GPIO.output(self.IN4B, GPIO.LOW)
    
    def rotate_180cw(self, speed=0, t=0):#letter l
        #1. activate pwm
        #2. set the required pins to HIGH and LOW
        self.PWM1A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1A, GPIO.HIGH) #front RIGHT
        GPIO.output(self.IN2A, GPIO.LOW)

        self.PWM2A.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3A, GPIO.LOW) #front LEFT
        GPIO.output(self.IN4A, GPIO.HIGH)

        self.PWM1B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN1B, GPIO.HIGH) #back right
        GPIO.output(self.IN2B, GPIO.LOW)

        self.PWM2B.ChangeDutyCycle(abs(speed))
        GPIO.output(self.IN3B, GPIO.HIGH) #back left
        GPIO.output(self.IN4B, GPIO.LOW)

def main():
        motors.Forward(40, 2) #spins with a pwm of 60 for 3 seconds
        motors.stop(2)
    

if __name__ == '__main__':
    motors = Motor(14,7,1,20,21,15,3,26,19,13,6,4) #pins 
    main()

GPIO.cleanup()