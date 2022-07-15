import pygame
import joystick_module as jsm
import motor_module as mm
import cv2 as cv
from time import sleep

maxThrottle = 0.25
motor = mm.Motor(2,3,4,17, 27, 22)

record = 0

while True:
    joyVal = jsm.getJS()
    steering = joyVal['axis2']
    throttle = joyVal['o']*maxThrottle

    if joyVal['share'] == 1:
        if record ==0: print('Recording Started ...')
        record += 1
        sleep(0.300)
    if record==1:
        img = wm.getImg(True,size=(240,120))
        dcM.saveData(img,steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle, -steering)
    cv.waitKey(1)