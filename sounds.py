import pygame
from pygame.mixer import Sound
from gpiozero import MotionSensor
from time import sleep
import random

pygame.init()
pygame.mixer.init()
#load a sound file, same directory as script (no mp3s)

sounds = [
        pygame.mixer.Sound("/home/pi/hp1.wav"),
        pygame.mixer.Sound("/home/pi/loo.ogg"),
#        pygame.mixer.Sound("/home/pi/puzzled.wav"),
        pygame.mixer.Sound("/home/pi/changes.ogg"),
        pygame.mixer.Sound("/home/pi/train1.wav")
        ]


pir = MotionSensor(23)
while True:
    if pir.motion_detected:
        print ("No motion")
    else:
        print("Motion detected!")
        playSound = random.choice(sounds)
	playSound.play().set_volume(1.0)
        # ensure playback has been fully completed before resuming motion detection, prevents "spamming" of sound
        sleep(8)
        playSound.stop()

