import time
import adafruit_dht
from board import *
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

dhtDevice = adafruit_dht.DHT11(D4, use_pulseio=False)
  
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
#font = imageFont.truetype('Maplestory Bold.ttf',10)
font = ImageFont.load_default()

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        temperatureStr = ("temp : {}C". format(temperature))
        humidityStr = ("Humidity : {}%". format(humidity))
        print("temp : {}C  Humidity : {}%". format(temperature, humidity))
        
        draw.text((0, 4),temperatureStr, font=font,fill=255)
        draw.text((0, 20),humidityStr, font=font,fill=255)
        display.image(image)
        display.show()
        
        time.sleep(2)
        draw.rectangle((0, 0, display.width, display.height), fill=0)
        
    except RuntimeError as error:
        pass
