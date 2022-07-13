import curses   #lib to read the key strokes
                # the lib/ module streams the keyboard
from RpiMotorLib import rpi_dc_lib                


screen = curses.initscr() # Get the curses window,
curses.noecho() # turn off echoing of the keyboard to screen
                # turn on instantly key response -> no waiting,
curses.cbreak() # use special values for cursor keys
screen.keypad(True)

def motor1():
    motorOne = rpi_dc_lib.L298NMDc(26,19,13,30,True,motor1)
    motorOne.forward(30)


try: #lets us check for errors
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print('up')
            motor1()
        elif char == curses.KEY_DOWN:
            print ("down")
        elif char == curses.KEY_RIGHT:
            print("right")
        elif char == curses.KEY_LEFT:
            print("left")
        elif char == 10: #the enter key
            print("stop")
finally:
    #close down curses properly.
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()