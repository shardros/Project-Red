import RPi.GPIO as GPIO
import time

logLvl = 2
"""
2 - All
1 - Some
0 - None
"""

"""
NOTE the cube is defined as follows:

    FRONT

----ROW 0----
----ROW 1----
----ROW 2----
----ROW 3----
  3  2  1  0

The layers are numbered bottom up
"""

pins = [13, 15, 19, 21,  # 0th row
        23, 29, 31, 33,  # 1st row
        35, 37, 8, 10,  # 2nd row
        12, 16, 18, 22,  # 3rd row
        3, 5, 7, 11,  # Layer GPIO
        24, 26, 32, 36,
        38, 40]


class Led:
    """
    This Class is for use of the cube class which is its parent class
    """

    state = 0

    def __init__(self, row, collum, layer):
        """
        :param row: The LEDs position
        :param collum: The LEDs position
        :param layer: The LEDs position
        """
        if logLvl > 0: print("Init method of LED class called")
        self.row = row
        self.collum = collum
        self.layer = layer
        self.horizontal_pin = self.collum + (4 * self.collum)

    def setLed(self, state):
        """
        :param state: state holds the state the LED is to be self.sate is the current state
        :return: null or exception
        """
        if state == (1 or "HIGH" or "high" or "ON" or "on"):
            state = 1
        elif state == (0 or "LOW" or "low" or "OFF" or "off"):
            state = 0
        else:
            raise NameError("Invalid state set for pin")

        state = 1
        # Set the varible that holds the state we will have to have a refresh system that goes over this an outputs all of the states
        if logLvl == 2: print("set led to ", state)


class Cube:
    """
    Cube Class:
    -Second level hardware abstraction cube for higher level interactiosn and manipulation
    -Allows for software based PWM for the animations
    """

    def __init__(self):
        print("init method of Cube class called")
        GPIO.setmode(GPIO.BOARD)

        # Sets the All the pins that are defined to be outputs
        for i in range(0, len(pins)):
            GPIO.setup(pins[i], GPIO.OUT)

        # Init array of 4*4*4 with LED objects in the array
        leds = [[[Led(i, j, k) for k in range(0, 4)] for j in range(0, 4)] for i in range(0, 4)]