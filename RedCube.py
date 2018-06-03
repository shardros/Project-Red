import RPi.GPIO as GPIO
import time

logLvl = 0
"""
0 - All
1 - Pin actions
2 - Methods
3 - none
"""

pins = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37, 8, 10, 12, 16, 18, 22, 24, 26, 32, 36, 38, 40]


class Cube:
    """
    Dark Class:
    -First level hardware abstraction cube for higher level interactiosn and manipulation
    -Allows for software based PWM for the animations
    """
    leds = [
        [
            [3, 3, 3, 3],
            [3, 3, 3, 3],
            [3, 3, 3, 3]],
        [
            [3, 3, 3, 3],
            [3, 3, 3, 3],
            [3, 3, 3, 3]],
        [
            [3, 3, 3, 3],
            [3, 3, 3, 3],
            [3, 3, 3, 3]
        ]]

    def __init__(self):
        print("init method of Cube class called")
        GPIO.setmode(GPIO.BOARD)
        for i in range(0, len(self.leds)):
            GPIO.setup(self.leds[i], GPIO.OUT)
            print("Pin ", i, " configured as output")

    def setLed(self, led, state):
        if state == (1 or "HIGH" or "high" or "ON" or "on"):
            state = 1
        elif state == (0 or "LOW" or "low" or "OFF" or "off"):
            state = 0
        else:
            raise NameError("Invalid state set for led ", str(led))
        GPIO.output(self.leds[led], state)
        print("set pin ", str(led), " to ", state)


