import motor_module
import keyboard_module as kb

from motor_module import Motor


#create the motor and pass in the parameters
motor1 = Motor(2,3,4,17, 22, 27)

kb.init()
def main():
    ####TEST CODE###
    # kb.getKey()
    # motor1.moveFoward(0.6, 5)
    # motor1.stop(3)
    if kb.getKey('UP'):
        motor1.moveFoward(0.6, 0, 0.1) #move upon the keypress time value of max 0.1 s after release
    elif kb.getKey('DOWN'):
        motor1.moveFoward(-0.6, 0, 0.1)
    else:
        motor1.stop(0.1)




if __name__ == '__main__':
    while True:
        main()