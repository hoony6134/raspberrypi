from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
 
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

width = display.width
height = display.height

image = Image.new("1", (width, height))
 
draw = ImageDraw.Draw(image)
 
while True:
    image = Image.open('bat.png').resize((width, height),Image.ANTIALIAS).convert('1')
    display.image(image)
    display.show()