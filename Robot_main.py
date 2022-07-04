import motor_module

from motor_module import Motor

#create the motor and pass in the parameters
motor1 = Motor(2,3,4,17, 22, 27)

motor1.moveFoward(0.6, 5)
motor1.stop(3)