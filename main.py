import RPi.GPIO as GPIO
import time

pins=[3,5,7,11,13,15,19,21,23,29,31,33,35,37,8,10,12,16,18,22,24,26,32,36,38,40]


GPIO.setmode(GPIO.BOARD)

for i in range (0,len(pins)):
	GPIO.setup(pins[i],GPIO.OUT)
	GPIO.output(pins[i],GPIO.HIGH)
	print("set pin " , str(pins[i]), "to high")


time.sleep(120)

GPIO.cleanup()
