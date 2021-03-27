import time
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LIGHT_PIN = 14

GPIO.setup(LIGHT_PIN, GPIO.IN)
pixel_pin = board.D18

num_pixels = 7
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
        
while True:
    try:
        if GPIO.input(LIGHT_PIN):
            print('Dark')
            pixels.fill((255, 255, 255))
            pixels.show()
        else:
            print('Bright')
            pixels.fill((0, 0, 0))
            pixels.show()
        time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('clean')
        break