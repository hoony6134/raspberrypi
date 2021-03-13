from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(alpha=192)
for i in range(5):
    sleep(2)
    camera.capture("/home/pi/Desktop/test%s.jpg" % i)
camera.stop_preview()
