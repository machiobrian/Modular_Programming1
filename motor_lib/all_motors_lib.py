from time import sleep
from RpiMotorLib import rpi_dc_lib


def motor1():
    #define motor instance
    motorOne = rpi_dc_lib.L298NMDc(26,19,13,30,True,motor1)
    
    try:
        motorOne.forward(30)
        input("press key to stop")
        #pressing any key stops the motor
        motorOne.stop(0)
        sleep(2)

        motorOne.backward(30)
        input("press key to stop")
        #press any key to stop
        motorOne.stop(0)
        sleep(2)

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    else:
        print('no errors')
    
    finally:
        motorOne.cleanup(True)

def motor2():
    #define motor instance
    motorTwo = rpi_dc_lib.L298NMDc(26,19,13,30,True,motor1)
    
    try:
        motorTwo.forward(30)
        input("press key to stop")
        #pressing any key stops the motor
        motorTwo.stop(0)
        sleep(2)

        motorTwo.backward(30)
        input("press key to stop")
        #press any key to stop
        motorTwo.stop(0)
        sleep(2)

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    else:
        print('no errors')
    
    finally:
        motorTwo.cleanup(True)

def motor3():
    #define motor instance
    motorThree = rpi_dc_lib.L298NMDc(26,19,13,30,True,motor1)
    
    try:
        motorThree.forward(30)
        input("press key to stop")
        #pressing any key stops the motor
        motorThree.stop(0)
        sleep(2)

        motorThree.backward(30)
        input("press key to stop")
        #press any key to stop
        motorThree.stop(0)
        sleep(2)

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    else:
        print('no errors')
    
    finally:
        motorThree.cleanup(True)

def motor4():
    #define motor instance
    motorFour = rpi_dc_lib.L298NMDc(26,19,13,30,True,motor1)
    
    try:
        motorFour.forward(30)
        input("press key to stop")
        #pressing any key stops the motor
        motorFour.stop(0)
        sleep(2)

        motorFour.backward(30)
        input("press key to stop")
        #press any key to stop
        motorFour.stop(0)
        sleep(2)

    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    else:
        print('no errors')
    
    finally:
        motorFour.cleanup(True)


if __name__ == '__main__':

    # motor1()
    # motor2()
    # motor3()
    motor4()

    exit()
