# 9am - 5pm
# water- 3.5 ltr
# eye = eyes.mp3 - 30min
# excercise - physical.mp3 - 45min

# pygame module play mp3

# import pygame, sys, time
# from pygame.locals import *

# pygame.init()

# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Memes.')


# pygame.mixer.music.load("dard.mp3")
# pygame.mixer.music.play()
# time.sleep(2)
# # pygame.mixer.music.stop()

# while True: # Main Loop

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()


# ------------------------------------------------------------------
# play mp3 
#install pygame , pip install pygame

import time
from pygame import mixer

def play(soundfile, duration_secs):
    """Play a soundfile for a configurable duration""" 
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()

# Play for 5 seconds
play('D:\\python_programs\\dard.mp3', 3)

import datetime
tday = datetime.datetime.today()
set_time = tday.replace(hour=17,minute=27)
print(set_time)

if set_time == datetime.datetime.now():
	print("sahi")
	play('D:\\python_programs\\dard.mp3', 3)