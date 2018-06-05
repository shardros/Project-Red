import RedCube
import RPi.GPIO as GPIO

try:
    c = RedCube.Cube()
    for i in range (0,len(c.leds)):
        c.leds[i].state = 1
    while True:
        c.refresh()
except:
    GPIO.cleanup()
