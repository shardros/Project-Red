#Import modules
import RPi.GPIO  as GPIO
import time

#Set-up of modules
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#Init global lists
cube = [[[0 for k in xrange(4)] for j in xrange(4)] for i in xrange(4)]
layer_pins = [29, 31, 33, 35] 
collum_pins = [10, 7, 26, 36, 11, 8, 23, 32, 13, 5, 21, 22, 3, 15, 24, 37]
	      
for i in range(0,len(layer_pins)):
	#Setup the layers and turn the pins high
	GPIO.setup(layer_pins[i], GPIO.OUT)
	GPIO.output(layer_pins[i], 1)
	print("Setup pin ", str(layer_pins[i]), " as output and set it to one")


for i in range(0,len(collum_pins)):
	GPIO.setup(collum_pins[i], GPIO.OUT)
	GPIO.output(collum_pins[i], 0)
	print("Setup pin ", str(collum_pins[i]), " as output and set it to zero")


def wipe():
	for i in range(0, len(collum_pins)):
		GPIO.output(collum_pins[i], 1)
		time.sleep(0.025)

try:
	for i in range(0, len(collum_pins)):
		GPIO.output(collum_pins[i], 1)
		print("set pin ", str(i), " high")
		time.sleep(0.5)
#		GPIO.output(collum_pins[i], 0)
except:
	print("INTERPUT")
	GPIO.cleanup()
