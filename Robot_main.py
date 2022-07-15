import motor_module as mm
import keyboard_module as kb
import joystick_module as jsm

from all_motors import Motor


#create the motor and pass in the parameters
motors = Motor(14,7,1,20,21,15,3,26,19,13,6,4)

# kb.init()
# def main():
#     ####TEST CODE###
#     # kb.getKey()
#     # motor1.moveFoward(0.6, 5)
#     # motor1.stop(3)
#     if kb.getKey('UP'):
#         print('up')
#         motors.Forward(60,0.1) #move upon the keypress time value of max 0.1 s after release
    
#     if kb.getKey('RIGHT'):
#         print('right')
#         motors.moveRight(60,0.1)

#     if kb.getKey('DOWN'):
#         print('down')
#         motors.moveRight(60,0.1)

#     if kb.getKey('LEFT'):
#         print('left')
#         motors.moveRight(60,0.1)
    
#     else:
#         motors.stop(0.1)

maxThrottle = 0.25
motor = mm.Motor(14,7,1,20,21,15,3,26,19,13,6,4)

if __name__ == '__main__':
    while True:
        joyVal = jsm.getJS()
        steering = joyVal['axis2']
        throttle = joyVal['o']*maxThrottle

        motor.move(steering, throttle, 1)