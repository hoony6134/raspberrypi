import RPi.GPIO as GPIO

servoPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)

pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)

try:
    while True:
        position = float(input('sevo angle (2.5 ~ 12.5) : '))
        pwm.ChangeDutyCycle(position)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()