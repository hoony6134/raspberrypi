import time
import board
import neopixel
import random

pixel_pin = board.D18

num_pixels = 7
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)

def cycle(wait):
    for i in range(num_pixels):
        pixels[i] = (
            random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        pixels.show()
        time.sleep(wait)
        
while True:
    cycle(0.1)