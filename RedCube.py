import RPi.GPIO as GPIO
import time

logLvl = 2
"""
2 - All
1 - Some
0 - None
"""

pins = [3, 5, 7, 11, #Layer GPIO
        13, 15, 19, 21, 23, 29, 31, 33, 35, 37, 8, 10, 12, 16, 18, 22, 24, 26, 32, 36, 38, 40]

class Led:
    """
    This Class is for use of the cube class which is its parent class
    """

    state = 0

    def __init__(self, pin):
        if logLvl > 0: print("Init method of LED class called")
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        if logLvl > 0: print("Pin ", self.pin, " configured as output")

    def setLed(self, state):
        """
        :param state: state holds the state the LED is to be self.sate is the current state
        :return: null
        """
        if state == (1 or "HIGH" or "high" or "ON" or "on"):
            state = 1
        elif state == (0 or "LOW" or "low" or "OFF" or "off"):
            state = 0
        else:
            raise NameError("Invalid state set for pin ", str(self.pin))
        GPIO.output(self.pin, state)
        if logLvl == 2: print("set pin ", str(self.pin), " to ", state)


class Cube:
    """
    Cube Class:
    -Second level hardware abstraction cube for higher level interactiosn and manipulation
    -Allows for software based PWM for the animations
    """

    def __init__(self):
        print("init method of Cube class called")
        GPIO.setmode(GPIO.BOARD)
        



