from picamera import PiCamera
import time
import RPi.GPIO as GPIO
import board
import neopixel

soundSensor = 17
pixel_pin = board.D18
num_pixels = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(soundSensor, GPIO.IN)

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=2, auto_write=True, pixel_order=ORDER)


while True:
    if GPIO.input(soundSensor):
        print('Noisy')
        camera = PiCamera()
        camera.start_preview(alpha=192)
        pixels.fill((255, 0, 0))
        time.sleep(2)
        camera.capture("/home/pi/Desktop/test.jpg")
        camera.stop_preview()
        camera.close()
    else:
        print('Quiet')
        pixels.fill((0, 0, 0))
    time.sleep(0.1)


