import time
from board import * 
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(D4, use_pulseio=False)

while True:
    try:
         temperature = dhtDevice.temperature
         humidity = dhtDevice.humidity
         print("temp : {}C  Humidity : {}%". format(temperature, humidity))
    except RuntimeError as error:
        pass
    time.sleep(1)
    