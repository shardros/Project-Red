import RPi.GPIO as GPIO
import time

collum_pins = []
layer_pins = [29, 31, 33, 35]

GPIO.setmode(GPIO.BOARD)

for i in range(0,4):
    GPIO.setup(layer_pins[i], GPIO.OUT)

j = 3

while True:
    for i in range(0 ,4):
        GPIO.output(layer_pins[i], 1)
        GPIO.output(layer_pins[j], 0)
        j = i
        print("moved to next layer")
        time.sleep(1)