from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.annotate_text_size = 50
camera.annotate_text = "Hello World"
sleep(5)
camera.capture("/home/pi/Desktop/imgText.jpg")
camera.stop_preview

