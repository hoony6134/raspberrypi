import time
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pixel_pin = board.D18

LIGHT_PIN = 14
num_pixels = 7

GPIO.setup(LIGHT_PIN, GPIO.IN)
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

while True:
    try:
        if GPIO.input(LIGHT_PIN):
            pixels.fill((150, 150, 200))
            pixels.show()
        else:
            pixels.fill((0, 0, 0))
            pixels.show()
        
        time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('clean')
        break
