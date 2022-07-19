import sys, tty, termios
from gpiozero import Motor, PWMOutputDevice
from time import sleep
pwm_pin = 10

#motor pins
m_f_l = [9,11]
m_f_r = [0,5]
m_r_r = [6,13]
m_r_l = [19,26]

motors = [
    Motor(m_f_l[1], m_f_l[0], pwm=False),
    Motor(m_f_r[0], m_f_r[1], pwm=False),
    Motor(m_r_l[0], m_r_l[1], pwm=False),
    Motor(m_r_r[0], m_r_r[1], pwm=False)
]

pwm_out = PWMOutputDevice(pwm_pin)

#get a char from the command line
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch

#list to convert key into motor on/off values to correspond with direction
#direction based on number keypad

direction = {
    '1' : "turn_left",
    '2' : "backward",
    '3' : "turn_right",
    '4' : "left",
    '5' : "stop",
    '6' : "right",
    '7' : "diagonal_left",
    '8' : "forward",
    '9' : "diagonal_right",
    'q' : "diagonal_left",
    'e' : "diagonal_right",
    'z' : "diagonal_left_rev",
    'c' : "diagonal_right_rev"
}

current_dir = "stop"

#speed is a percentage i.e. 100 -> top speed
#start speed is 50% -> fairly slow on flat surface
speed = 10
pwm_out.value = (speed/100)

while True:
    #convert the speed from % to float 0 to 1
    if (current_dir == "forward"):
        motors[0].forward()
        motors[1].forward()
        motors[2].forward()
        motors[3].forward()
     #   sleep(0.3)
    # rev
    elif (current_dir == "backward") :
        motors[0].backward()
        motors[1].backward()
        motors[2].backward()
        motors[3].backward()
    #    sleep(0.3)
    elif (current_dir == "left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].forward()
        motors[3].backward()
   #     sleep(0.3)
    elif (current_dir == "right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].forward()
        motors[3].backward()
        sleep(0.3)
    elif (current_dir == "diagonal_left") :
        motors[0].stop()
        motors[1].forward()
        motors[2].forward()
        motors[3].stop()
    #    sleep(0.3)
    elif (current_dir == "diagonal_right") :
        motors[0].forward()
        motors[1].stop()
        motors[2].stop()
        motors[3].forward()
       # sleep(0.3)
    elif (current_dir == "diagonal_right_rev") :
        motors[0].stop()
        motors[1].backward()
        motors[2].backward()
        motors[3].stop()
       # sleep(0.3)
    elif (current_dir == "diagonal_left_rev") :
        motors[0].backward()
        motors[1].stop()
        motors[2].stop()
        motors[3].backward()
        #sleep(0.3)
    # stop
    else :
        motors[0].stop()
        motors[1].stop()
        motors[2].stop()
        motors[3].stop()
       # sleep(0.5)

    #check the next key press
    ch = getch()

    #p = quit
    if(ch == 'p'):
        break

    #alter the speed using - and = 
    elif (ch == '='):
        speed += 10
        if speed > 100:
            speed = 100
        pwm_out.value = speed/100
        #print('speed : '+str(speed))

    elif (ch == '-'):
        speed -= 10
        if speed < 0 :
            speed = 0
        pwm_out.value = speed/100
    elif (ch in direction.keys()):
        current_dir = direction[ch]
        print('Direction '+current_dir)
import sys, tty, termios
from gpiozero import Motor, PWMOutputDevice
from time import sleep
pwm_pin = 10

#motor pins
m_f_l = [9,11]
m_f_r = [0,5]
m_r_r = [6,13]
m_r_l = [19,26]

motors = [
    Motor(m_f_l[1], m_f_l[0], pwm=False),
    Motor(m_f_r[0], m_f_r[1], pwm=False),
    Motor(m_r_l[0], m_r_l[1], pwm=False),
    Motor(m_r_r[0], m_r_r[1], pwm=False)
]

pwm_out = PWMOutputDevice(pwm_pin)

#get a char from the command line
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch

#list to convert key into motor on/off values to correspond with direction
#direction based on number keypad

direction = {
    '1' : "turn_left",
    '2' : "backward",
    '3' : "turn_right",
    '4' : "left",
    '5' : "stop",
    '6' : "right",
    '7' : "diagonal_left",
    '8' : "forward",
    '9' : "diagonal_right",
    'q' : "diagonal_left",
    'e' : "diagonal_right",
    'z' : "diagonal_left_rev",
    'c' : "diagonal_right_rev"
}

current_dir = "stop"

#speed is a percentage i.e. 100 -> top speed
#start speed is 50% -> fairly slow on flat surface
speed = 10
pwm_out.value = (speed/100)

while True:
    #convert the speed from % to float 0 to 1
    if (current_dir == "forward"):
        motors[0].forward()
        motors[1].forward()
        motors[2].forward()
        motors[3].forward()
     #   sleep(0.3)
    # rev
    elif (current_dir == "backward") :
        motors[0].backward()
        motors[1].backward()
        motors[2].backward()
        motors[3].backward()
    #    sleep(0.3)
    elif (current_dir == "left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].forward()
        motors[3].backward()
   #     sleep(0.3)
    elif (current_dir == "right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].forward()
        motors[3].backward()
        sleep(0.3)
    elif (current_dir == "diagonal_left") :
        motors[0].stop()
        motors[1].forward()
        motors[2].forward()
        motors[3].stop()
    #    sleep(0.3)
    elif (current_dir == "diagonal_right") :
        motors[0].forward()
        motors[1].stop()
        motors[2].stop()
        motors[3].forward()
       # sleep(0.3)
    elif (current_dir == "diagonal_right_rev") :
        motors[0].stop()
        motors[1].backward()
        motors[2].backward()
        motors[3].stop()
       # sleep(0.3)
    elif (current_dir == "diagonal_left_rev") :
        motors[0].backward()
        motors[1].stop()
        motors[2].stop()
        motors[3].backward()
        #sleep(0.3)
    # stop
    else :
        motors[0].stop()
        motors[1].stop()
        motors[2].stop()
        motors[3].stop()
       # sleep(0.5)

    #check the next key press
    ch = getch()

    #p = quit
    if(ch == 'p'):
        break

    #alter the speed using - and = 
    elif (ch == '='):
        speed += 10
        if speed > 100:
            speed = 100
        pwm_out.value = speed/100
        #print('speed : '+str(speed))

    elif (ch == '-'):
        speed -= 10
        if speed < 0 :
            speed = 0
        pwm_out.value = speed/100
    elif (ch in direction.keys()):
        current_dir = direction[ch]
        print('Direction '+current_dir)
import sys, tty, termios
from gpiozero import Motor, PWMOutputDevice
from time import sleep
pwm_pin = 10

#motor pins
m_f_l = [9,11]
m_f_r = [0,5]
m_r_r = [6,13]
m_r_l = [19,26]

motors = [
    Motor(m_f_l[1], m_f_l[0], pwm=False),
    Motor(m_f_r[0], m_f_r[1], pwm=False),
    Motor(m_r_l[0], m_r_l[1], pwm=False),
    Motor(m_r_r[0], m_r_r[1], pwm=False)
]

pwm_out = PWMOutputDevice(pwm_pin)

#get a char from the command line
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch

#list to convert key into motor on/off values to correspond with direction
#direction based on number keypad

direction = {
    '1' : "turn_left",
    '2' : "backward",
    '3' : "turn_right",
    '4' : "left",
    '5' : "stop",
    '6' : "right",
    '7' : "diagonal_left",
    '8' : "forward",
    '9' : "diagonal_right",
    'q' : "diagonal_left",
    'e' : "diagonal_right",
    'z' : "diagonal_left_rev",
    'c' : "diagonal_right_rev"
}

current_dir = "stop"

#speed is a percentage i.e. 100 -> top speed
#start speed is 50% -> fairly slow on flat surface
speed = 10
pwm_out.value = (speed/100)

while True:
    #convert the speed from % to float 0 to 1
    if (current_dir == "forward"):
        motors[0].forward()
        motors[1].forward()
        motors[2].forward()
        motors[3].forward()
     #   sleep(0.3)
    # rev
    elif (current_dir == "backward") :
        motors[0].backward()
        motors[1].backward()
        motors[2].backward()
        motors[3].backward()
    #    sleep(0.3)
    elif (current_dir == "left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].forward()
        motors[3].backward()
   #     sleep(0.3)
    elif (current_dir == "right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_left") :
        motors[0].backward()
        motors[1].forward()
        motors[2].backward()
        motors[3].forward()
     #   sleep(0.3)
    elif (current_dir == "turn_right") :
        motors[0].forward()
        motors[1].backward()
        motors[2].forward()
        motors[3].backward()
        sleep(0.3)
    elif (current_dir == "diagonal_left") :
        motors[0].stop()
        motors[1].forward()
        motors[2].forward()
        motors[3].stop()
    #    sleep(0.3)
    elif (current_dir == "diagonal_right") :
        motors[0].forward()
        motors[1].stop()
        motors[2].stop()
        motors[3].forward()
       # sleep(0.3)
    elif (current_dir == "diagonal_right_rev") :
        motors[0].stop()
        motors[1].backward()
        motors[2].backward()
        motors[3].stop()
       # sleep(0.3)
    elif (current_dir == "diagonal_left_rev") :
        motors[0].backward()
        motors[1].stop()
        motors[2].stop()
        motors[3].backward()
        #sleep(0.3)
    # stop
    else :
        motors[0].stop()
        motors[1].stop()
        motors[2].stop()
        motors[3].stop()
       # sleep(0.5)

    #check the next key press
    ch = getch()

    #p = quit
    if(ch == 'p'):
        break

    #alter the speed using - and = 
    elif (ch == '='):
        speed += 10
        if speed > 100:
            speed = 100
        pwm_out.value = speed/100
        #print('speed : '+str(speed))

    elif (ch == '-'):
        speed -= 10
        if speed < 0 :
            speed = 0
        pwm_out.value = speed/100
    elif (ch in direction.keys()):
        current_dir = direction[ch]
        print('Direction '+current_dir)
