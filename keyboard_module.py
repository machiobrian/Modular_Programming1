#must in the longrun interact with the motor

#using pygame, 

import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100)) #we need a window to detect the keypresses on

def getKey(keyName):
    ans = False #initiate the key as not pressed
    for eve in pygame.event.get():pass #get all the events 
    keyInput = pygame.key.get_pressed() #from the events get the pressed events
                                    #to have a general key function
    myKey = getattr(pygame,'K_{}'.format(keyName)) #the keyname value will go into the 
                                    #bracket -> this is made sure by the .format(keyName)

    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():

    steering = 0
    if getKey('LEFT'):
        steering = -100
        print('LEFT')
    if getKey ('RIGHT'):
        steering = 100
        print('RIGHT')
    if getKey ('UP'):
        steering = 100
        print('UP')
    if getKey ('DOWN'):
        steering = -100
        print(steering)
        print('DOWN')
    

if __name__ == '__main__':
    init()
    while True:
        main()