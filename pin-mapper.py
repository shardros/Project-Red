#Import modules
import RPi.GPIO  as GPIO
import time

#Set-up of modules
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#Init global lists
cube = [[[0 for k in xrange(4)] for j in xrange(4)] for i in xrange(4)]
layer_pins = [29, 31, 33, 35] 
collum_pins = [13, 15, 19, 21,  # 0th row
        23, 37, 8, 10,  # 2nd row
        12, 16, 18, 22,  # 3rd row
        3, 5, 7, 11,  # Layer GPIO
        24, 26, 32, 36,
        38, 40] 

ordered_collum_pins = [3 for i in xrange(16)]

for i in range(0,len(layer_pins)):
	#Setup the layers and turn the pins high
	GPIO.setup(layer_pins[i], GPIO.OUT)
	GPIO.output(layer_pins[i], 1)

for i in range(0,len(collum_pins)):
	GPIO.setup(collum_pins[i], GPIO.OUT)
	GPIO.output(collum_pins[i], 0)
	print("Setup pin ", str(collum_pins[i]), " as output and set it to zero")

for i in range(0,len(collum_pins)):
	GPIO.output(collum_pins[i], 1)
	row = input("ROW: ")
	collum_in_row = input("Collum in row: ")
	ordered_collum_pins[(collum_in_row - 1) + (4 * (row - 1))] = collum_pins[i]
	GPIO.output(collum_pins[i], 0)

print(ordered_collum_pins)
GPIO.cleanup()
