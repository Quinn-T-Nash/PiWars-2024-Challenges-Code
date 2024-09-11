# Custom control program for Hal 4.5
# Based on the ps4.py program in the RedRobotics folder
# Author: Jason Stephens

from __future__ import print_function  # Make print work with python 2 & 3
from evdev import InputDevice, ecodes
import time
import redboard

dev = InputDevice('/dev/input/event2')
#print(dev)

device = str(dev).find('Wireless Controller')
if device != -1:
    print ('Controller: PS3 Gamepad')

# Map buttons
triangle, x, square, circle = 300, 302, 303, 301
R1, R2, R3 = 299, 297, 290
L1, L2, L3 = 298, 296, 289
select, start, PSbutton = 288, 291, 304
dup, ddown, dleft, dright = 292, 294, 295, 293

# Set up variables
RX = 0
LX = 0
RY = 0
LY = 0
LeftY = 0
RightY = 0
Leftmotor = 0
Rightmotor = 0
LM_OLD = 0
RM_OLD = 0
turbo = False

Max_Speed = 100

#Main play loop
for event in dev.read_loop():
    #print(event)  # Uncomment to show all button data

    #If/else to read button presses and do things
    if event.type == ecodes.EV_KEY:
        #print(event.code)  # Uncomment to show each keycode
        if event.value == 1:  # Button pressed
            if event.code == triangle:
                print ('triangle')
            elif event.code == x:
                print ('X')
            elif event.code == square:
                print ('Square')
            elif event.code == circle:
                print ('Circle')
                turbo = not turbo
            elif event.code == R1:
                print ('Right Turn')
            elif event.code == R2: 
                print ('R2')
            elif event.code == R3:
                print ('R3')
            elif event.code == L1:
                print ('L1')
            elif event.code == L2:
                print ('L2')
            elif event.code == L3:
                print ('L3')
            elif event.code == select:
                print ('Select')
            elif event.code == start:
                print ('Start')
            elif event.code == PSbutton:
                print ('PS Button')
            elif event.code == dup:
                print('D pad Up')
            elif event.code == ddown:
                print('D pad Down')
            elif event.code == dleft:
                print('D pad Left')
            elif event.code == dright:
                print('D pad Right')

    #Reads the position of the left and right joysticks and commands those motors to 
    #move accordingly
    if event.type == ecodes.EV_ABS:
        if event.code == 1:#See event code list below for details
            LeftY = event.value #Returns the position of the left y-axis on a scale of -127 to +127
            if LeftY > 10 or LeftY < -10: #Creates a dead zone on the joystick                
                if turbo:
                    CalcLeftY = LeftY * 0.7874 #Converts the position of the y-axis to a percentage between 0% and 100%
                    redboard.M1_8bit(-Max_Speed * CalcLeftY) #Sets the motor 1 speed based on position of the left joystick'''
                else:
                    CalcLeftY = LeftY * 0.02 #Converts the position of the y-axis to a percentage between 0% and 100%
                    redboard.M1_8bit(-Max_Speed * CalcLeftY) #Sets the motor 1 speed based on position of the left joystick'''
            else:
                    redboard.M1_8bit(0)
            print("Left Analog Y-axis = ", LeftY)
        if event.code == 3:
            RightY = event.value
            if RightY > 10 or RightY < -10:
                if turbo:
                    CalcRightY = RightY * 0.7874
                    redboard.M2_8bit(-Max_Speed * CalcRightY)  
                else:
                    CalcRightY = RightY * 0.02
                    redboard.M2_8bit(-Max_Speed * CalcRightY)                
            else:
                redboard.M2_8bit(0)
            print("Right Analog Y-axis = ", RightY)

#Left y axis = 1
#Left x axis = 0
#Right y axis = 3
#Right x axis = 2
