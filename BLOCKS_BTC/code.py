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
URL_BLOCKHEIGHT = "https://mempool.space/api/blocks/tip/height"
URL_PRICE = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
URL_PENDING_TXS = "https://bitcoinexplorer.org/api/mempool/count"

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


cycle = 0
cases = 2
while True:

    string = "0"
    #print("Fetching json from", URL)
    #response = requests.get(URL)
    #a = response.json()
    #btc_price = a['bitcoin']['usd']

    #print('This is BTC price: ' + str(btc_price))
    #string = str(btc_price)
    if cycle == 0:
        try:
            print ("Fetching block height from", URL_BLOCKHEIGHT)
            response = requests.get(URL_BLOCKHEIGHT)

            #decode from b'111111'
            string = response.content.decode()
            print('This is block height: ' + string)
        except:
            string = string
    elif cycle == 1:
        try:
            print("Fetching json from", URL_PRICE)
            response = requests.get(URL_PRICE)
            a = response.json()
            btc_price = a['bitcoin']['usd']
            string = str(btc_price)
            print('This is BTC price: ' + string )
        except:
            string = string
    elif cycle == 2:
        try:
            print ("Fetching pending txs from", URL_PENDING_TXS)
            response = requests.get(URL_PENDING_TXS)

            #decode from b'111111'
            string = str (response.content.decode() ) 
            print('This is number of pending txs: ' + string )
        except:
            string = string
    
    print ("String : " + string )
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

        #for y, row in enumerate(DOLLAR):
        #    for x, c in enumerate(row):
        #        display1.pixel(x + 0, y + 0, c)

    if cycle == 1:
        for y, row in enumerate(DOLLAR):
            for x, c in enumerate(row):
                display2.pixel(x - 35, y + 0, c)
    elif cycle == 0:
        for y, row in enumerate(SIXTH):
            for x, c in enumerate(row):
                display2.pixel(x - 5, y + 0, c)

    for y, row in enumerate(FIFTH):
        for x, c in enumerate(row):
            display2.pixel(x + 75, y + 0, c)

    for y, row in enumerate(FOURTH):
        for x, c in enumerate(row):
            display3.pixel(x - 5, y + 0, c)
    for y, row in enumerate(THIRD):
        for x, c in enumerate(row):
            display3.pixel(x + 75, y + 0, c)

    for y, row in enumerate(SECOND):
        for x, c in enumerate(row):
            display4.pixel(x - 5, y + 0, c)
    for y, row in enumerate(FIRST):
        for x, c in enumerate(row):
            display4.pixel(x + 75, y + 0, c)

    #for y, row in enumerate(BTC):
    #    for x, c in enumerate(row):
    #        display5.pixel(x + 0, y + 0, c)

    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

    print ( 'Cycle: ' + str(cycle) + ' done')


    if ( cycle < cases ):
        cycle+=1;
    elif ( cycle == cases ):
        cycle = 0;


    time.sleep(1)

