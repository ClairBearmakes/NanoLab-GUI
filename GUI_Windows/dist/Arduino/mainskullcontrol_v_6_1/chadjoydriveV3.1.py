#!/usr/bin/env python
import serial
import pygame
import subprocess
import time
import RPi.GPIO as GPIO
import subprocess
import sys
from pygame.locals import *
from array import *
# Initialise the pygame library

pygame.init()
GPIO.setwarnings(False)
# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()
numbuttons = j.get_numbuttons()
interval = 0.1
ser = serial.Serial('/dev/ttyACM0', 115200)

ser.write('n')
subprocess.call(["aplay", "/home/pi/Music/POWERUP.WAV"])
#time.sleep(3)
ser.write('t')
m = pygame.mixer.music
#m.load('/home/pi/Music/POWERUP.WAV')
#m.play(loops=0)
print 'Initialized Joystick : %s' % j.get_name()
threshold = 0.60
button = array("i")
Lmotor = 0
Rmotor = 0
interval = 0.05
LeftTrack = 0
RightTrack = 0


loopQuit = False
while loopQuit == False:

       

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          move = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              move = 1
            elif event.axis == 3:
              RightTrack = event.value
              move = 1

            # if joystick moved start a motor
            if move:     
 
              # Move right forward
              if (RightTrack > threshold):
                  ser.write('R')
              # Move right backward
              elif (RightTrack < -threshold):                                 
                  ser.write('r')
              # Stopping
              else:
                  ser.write('A')
              # Move left foward
              if (LeftTrack > threshold):
                  ser.write('L')
              # Move left backward
              elif (LeftTrack < -threshold):
                  ser.write('l')
              # Otherwise stop
              else:
                  ser.write('B')

              # Now we've worked out what is going on we can tell the
              # motors what they need to do
              
    

    
        for i in range(0,numbuttons):
            button.append(i)
            button[i] = j.get_button(i)

        if (button[8])==1:
             m.load('/home/pi/Music/sorry_to_hear.wav')
             m.play(loops=0)
        if (button[9])==1:
             ser.write('a')   
             m.load('/home/pi/Music/go_away.wav')
             time.sleep(.5)
             ser.write('o')           
             m.play(loops=0)
        if (button[3])==1:
            ser.write('a')
            subprocess.call(["espeak", "I am chad pi the cyborg"])
            ser.write('o')
        if (button[5])==1: #head up
            ser.write('e')
            time.sleep(.5)
            ser.write('o')
        if (button[7])==1:   #head down
            ser.write('d')
            time.sleep(.5)
            ser.write('o')
        if (button[4])==1:
            m.load('/home/pi/Music/talk_without_brain.wav')
            m.play(loops=0)
        if (button[0])==1:
            m.load('/home/pi/Music/fuss.wav')
            m.play(loops=0)
        if (button[2])==1:
            ser.write('a')
            subprocess.call(["espeak", "My nose itches"])
            time.sleep(1)
            ser.write('w')
            time.sleep(4)
            ser.write('a')
            subprocess.call(["espeak", "have you seen it"])
            ser.write('o')
            pygame.event.clear
            
            
        for event in pygame.event.get():
            if event.type == QUIT:
                loopQuit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loopQuit = True
    
        time.sleep(interval)
ser.write('n')
subprocess.call(["aplay", "/home/pi/Music/powerd.wav"])
ser.write('t')
pygame.quit()

