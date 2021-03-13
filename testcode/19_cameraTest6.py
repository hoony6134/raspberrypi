from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.exposure_mode = 'snow'
sleep(5)
camera.capture('/home/pi/Desktop/mode.jpg')
camera.stop_preview()

