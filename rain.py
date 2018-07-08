
#Import modules
import RPi.GPIO  as GPIO
import time
import random

#Set-up of modules
GPIO.setmode(GPIO.BOARD)

#Init globals 
cube = [[[0 for k in xrange(4)] for j in xrange(4)] for i in xrange(4)]
layer_pins = [29, 33, 31, 35] 
collum_pins = [[10, 7, 26, 40], [11, 8, 38, 36], [13, 5, 32, 22], [3, 15, 24, 37]]

frame_rate = 60


for i in range(0,len(layer_pins)):
	#Setup the layers and turn the pins high
	GPIO.setup(layer_pins[i], GPIO.OUT)
	GPIO.output(layer_pins[i], 1)
	print("Setup pin ", str(layer_pins[i]), " as output and set it to one")


for i in xrange(4):
		for j in xrange(4):	
				GPIO.setup(collum_pins[i][j], GPIO.OUT)
				GPIO.output(collum_pins[i][j], 0)
				print("Setup pin ", str(collum_pins[i][j]), " as output and set it to zero")
		
def refresh():
	for layer in xrange(4):
		GPIO.output(layer_pins[layer], 1)		
		for row in xrange(4):
			for collum in xrange(4):
				GPIO.output(collum_pins[row][collum], cube[layer][row][collum])


		time.sleep(1.0/(frame_rate*4))
		GPIO.output(layer_pins[layer], 0)


def wait(time):
	#time: the time to be waited in seconds
	for i in range(0,int(round(frame_rate*time))):
		refresh()


try:
	while True:
		row = [random.randrange(4) for i in xrange(2)]
		collum = [random.randrange(4) for i in xrange(2)]
		for test in range(3, -1, -1):
			cube[test][row[0]][collum[0]] = 1
			cube[test][row[1]][collum[1]] = 1
			wait(0.1)
			cube[test][row[0]][collum[0]] = 0
			cube[test][row[1]][collum[1]] = 0

except KeyboardInterrupt:
	print("INTERPUT")
	GPIO.cleanup()

