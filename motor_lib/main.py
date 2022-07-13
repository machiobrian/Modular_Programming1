import keyboard_module as kb
import all_motors_lib

from all_motors_lib import motor1, motor2, motor3, motor4

#create motor1 instance and pass in the module
# motor_1 = motor1()

kb.init()

def main():
    if kb.getKey('UP'):
        print('up')
        motor1()

if __name__=='__main__':
    while True:
        main()