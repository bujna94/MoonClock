import time
import os
import board
import busio
import adafruit_ssd1306
import adafruit_tca9548a

from numbers import *

import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests


# URLs to fetch from
JSON_QUOTES_URL = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

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

print("ESP32-S2 WebClient Test")

print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

print("Available WiFi networks:")
for network in wifi.radio.start_scanning_networks():
    print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
            network.rssi, network.channel))
wifi.radio.stop_scanning_networks()

print("Connecting to %s"%secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

def decide(number):
    if number == str(0):
        return ZERO
    elif number == str(1):
        return ONE
    elif number == str(2):
        return TWO
    elif number == str(3):
        return THREE
    elif number == str(4):
        return FOUR
    elif number == str(5):
        return FIVE
    elif number == str(6):
        return SIX
    elif number == str(7):
        return SEVEN
    elif number == str(8):
        return EIGHT
    elif number == str(9):
        return NINE
    elif number == str('.'):
        return DOT
        print('THIS IS DOT')

while True:


    print("Fetching json from", JSON_QUOTES_URL)
    response = requests.get(JSON_QUOTES_URL)

    a = response.json()

    doge_price = a['dogecoin']['usd']
    doge_price = ("%.3f" % doge_price)

    print('This is DOGE price: ' + str(doge_price))
    string = str(doge_price)

    try:
        FIRST = decide(string[-1])
        print('FIRST working')
    except:
        FIRST = EMPTY
        print('FIRST=EMPTY')

    try:
        SECOND = decide(string[-2])
        print('SECOND working')
    except:
        SECOND = EMPTY
        print('SECOND=EMPTY')

    try:
        THIRD = decide(string[-3])
        print('THIRD working')
    except:
        THIRD = EMPTY
        print('THIRD=EMPTY')

    try:
        FOURTH = decide(string[-4])
        print('FOURTH working')
    except:
        FOURTH = EMPTY
        print('FOURTH=EMPTY')

    try:
        FIFTH = decide(string[-5])
        print('FIFTH working')
    except:
        FIFTH = EMPTY
        print('FIFTH=EMPTY')

    try:
        SIXTH = decide(string[-6])
        print('SIXTH working')
    except:
        SIXTH = EMPTY
        print('SIXTH=EMPTY')

    display1.fill(0) # Clear the display
    display2.fill(0) # Clear the display
    display3.fill(0) # Clear the display
    display4.fill(0) # Clear the display
    display5.fill(0) # Clear the display
    try:
        for y, row in enumerate(DOLLAR):
            for x, c in enumerate(row):
                display1.pixel(x + 0, y + 0, c)
    except:
        print('problem with DOLLAR')

    try:
        for y, row in enumerate(SIXTH):
            for x, c in enumerate(row):
                display2.pixel(x - 5, y + 0, c)
    except:
        print('problem with SIXTH')

    try:
        for y, row in enumerate(FIFTH):
            for x, c in enumerate(row):
                display2.pixel(x + 81, y + 0, c)
    except:
        print('problem with FIFTH')

    try:
        for y, row in enumerate(FOURTH):
            for x, c in enumerate(row):
                display3.pixel(x + 15, y + 0, c)
    except:
        print('problem with FOURTH')

    try:
        for y, row in enumerate(THIRD):
            for x, c in enumerate(row):
                display3.pixel(x + 81, y + 0, c)
    except:
        print('problem with THIRD')

    try:
        for y, row in enumerate(SECOND):
            for x, c in enumerate(row):
                display4.pixel(x - 5, y + 0, c)
    except:
        print('problem with SECOND')

    try:
        for y, row in enumerate(FIRST):
            for x, c in enumerate(row):
                display4.pixel(x + 81, y + 0, c)
    except:
        print('problem with FIRST')

    try:
        for y, row in enumerate(DOGE):
            for x, c in enumerate(row):
                display5.pixel(x + 0, y + 0, c)
    except:
        print('problem with DOGE')

    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

    time.sleep(60)

