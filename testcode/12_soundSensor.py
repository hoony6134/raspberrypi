import time
import RPi.GPIO as GPIO

soundSensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(soundSensor, GPIO.IN)

while True:
    if GPIO.input(soundSensor):
        print('Noisy')
    else:
        print('Quiet')
    time.sleep(0.1)