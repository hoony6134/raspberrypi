from board import *
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
 
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
  
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Maplestory Bold.ttf',15)
 
while True:
    draw.text((4, 8),'Good', font=font,fill=255)
    display.image(image)
    display.show()
    
    