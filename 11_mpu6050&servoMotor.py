import RPi.GPIO as GPIO
import time
from math import atan2, degrees
import board
import busio
import adafruit_mpu6050
 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mpu6050.MPU6050(i2c)

servoPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)

pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)

def map(x,angle_min,angle_max,servo_min,servo_max):
    return (x-angle_min)*(servo_max-servo_min)/(angle_max-angle_min)+servo_min

try:
    while True:
        angle_xz, angle_yz = get_inclination(sensor)
        position = map(angle_yz,0, 360, 2.5, 12.5)
        pwm.ChangeDutyCycle(position)
        print(position)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    