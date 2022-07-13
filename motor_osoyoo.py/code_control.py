import code_motor
import RPi.GPIO as GPIO
from time import sleep

from code_motor import go_ahead, go_back, shift_left, shift_right, turn_left, turn_right

go_ahead(100)
sleep(1)
code_motor.stop_car()

go_back(100)
sleep(1)
code_motor.stop_car()

shift_left(60)
sleep(1)
code_motor.stop_car()

shift_right(100)
sleep(1)
code_motor.stop_car()

turn_left(100)
sleep(1)
code_motor.stop_car()

turn_right(100)
sleep(1)
code_motor.stop_car()

GPIO.cleanup()