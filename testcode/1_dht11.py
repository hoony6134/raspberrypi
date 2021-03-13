import time
from board import * 
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(D4, use_pulseio=False) #안되면 use_pulseio=True로 변경

while True:
    try:
         temperature = dhtDevice.temperature
         humidity = dhtDevice.humidity
         print("temp : {}C  Humidity : {}%". format(temperature, humidity))
    except RuntimeError as error:
        pass
    time.sleep(1)
    
