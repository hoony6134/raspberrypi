import board
import neopixel

pixel_pin = board.D18

num_pixels = 7

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=2, auto_write=True, pixel_order=ORDER)

pixels.fill((220, 220, 220))

