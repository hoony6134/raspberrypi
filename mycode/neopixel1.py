import board
import neopixel

pixel_pin = board.D18

num_pixels = 7

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=True, pixel_order=ORDER)

pixels.fill((100, 100, 100))