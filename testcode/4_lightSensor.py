import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT_PIN = 14

GPIO.setup(LIGHT_PIN, GPIO.IN)

while True:
    try:
        if GPIO.input(LIGHT_PIN):
            print('Dark')
        else:
            print('Bright')
        
        time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('clean')
        break



