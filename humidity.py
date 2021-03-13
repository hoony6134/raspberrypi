# ~$ pip3 install adafruit-circuitpython-dht
# ~$ sudo apt install libgpiod2
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)
while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("temp: {}C Humidity : {}%.".format(temperature_c, humidity))
    except RuntimeError as error:
        pass
    time.sleep(1)
