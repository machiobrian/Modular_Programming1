import code_control, code_motor
import code_js as js
from code_js import getJS
movement = 'JoyStick'
def main():
    if movement == 'JoyStick':
        print(getJS()) #prints the values of the joystick axes and buttons

        jsVal = getJS() #initialize a JS as getJS
        #to make our motor move with the code at joystick
        #have the values of js mapped to the motor move commands
        code_motor.fl_ahead(jsVal['axis4'])


