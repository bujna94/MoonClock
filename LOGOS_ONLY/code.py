import time
import os
import board
import busio
import adafruit_ssd1306
import adafruit_tca9548a

from numbers import *

WIDTH = 128
HEIGHT = 64
CENTER_X = int(WIDTH/2)
CENTER_Y = int(HEIGHT/2)

SDA = board.IO10
SCL = board.IO11

i2c = busio.I2C(SCL, SDA)

if(i2c.try_lock()):
    print("i2c.scan(): " + str(i2c.scan()))
    i2c.unlock()

tca = adafruit_tca9548a.TCA9548A(i2c)

display1 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[0])
display2 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[1])
display3 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[2])
display4 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[3])
display5 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[4])


while True:

    display1.fill(0) # Clear the display
    display2.fill(0) # Clear the display
    display3.fill(0) # Clear the display
    display4.fill(0) # Clear the display
    display5.fill(0) # Clear the display
    try:
        for y, row in enumerate(BTC):
            for x, c in enumerate(row):
                display1.pixel(x + 0, y + 0, c)
    except:
        print('problem with BTC')

    try:
        for y, row in enumerate(ETH):
            for x, c in enumerate(row):
                display2.pixel(x + 0, y + 0, c)
    except:
        print('problem with ETH')

    try:
        for y, row in enumerate(LTC):
            for x, c in enumerate(row):
                display3.pixel(x + 0, y + 0, c)
    except:
        print('problem with LTC')

    try:
        for y, row in enumerate(DOGE):
            for x, c in enumerate(row):
                display4.pixel(x + 0, y + 0, c)
    except:
        print('problem with DOGE')

    try:
        for y, row in enumerate(ADA):
            for x, c in enumerate(row):
                display5.pixel(x + 0, y + 0, c)
    except:
        print('problem with ADA')

    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

    time.sleep(60)

