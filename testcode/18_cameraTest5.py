from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.image_effect = 'cartoon'
sleep(5)
camera.capture('/home/pi/Desktop/effect.jpg')
camera.stop_preview()

