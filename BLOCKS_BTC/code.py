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
    elif number == str('$'):
        return DOLLAR
    elif number == str(':'):
        return LARGECOLON
    else:
        return EMPTY
        print ('this is empty or unsupported char')


def string_to_display (string, colon):
    centered_string = center ( string )

    print_display (display1, centered_string[0], centered_string[1]);
    print_display (display2, centered_string[2], centered_string[3]);
    print_display (display3, centered_string[4], centered_string[5]);
    print_display (display4, centered_string[6], centered_string[7]);
    print_display (display5, centered_string[8], centered_string[9]);

    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

    return 0

def time_to_display (string, colon):
    centered_string = center ( string )

    print_time (display1, centered_string[0], centered_string[1], 0);
    print_time (display2, centered_string[2], centered_string[3], 0);
    print_time (display3, centered_string[4], centered_string[5], 1);
    print_time (display4, centered_string[6], centered_string[7], 0);
    print_time (display5, centered_string[8], centered_string[9], 0);

    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

    return 0



def print_time (display, l1, l2, colon_boolean):
    bin_l1 = decide(l1)
    bin_l2 = decide(l2)

    display.fill(0) # Clear the display
    if colon_boolean:
        for y, row in enumerate(LARGECOLON):
            for x, c in enumerate(row):
                display.pixel(x + 0, y + 0, c)

    for y, row in enumerate(bin_l1):
        for x, c in enumerate(row):
            if (c == 1):
                display.pixel(x - 5, y + 0, c)

    for y, row in enumerate(bin_l2):
        for x, c in enumerate(row):
            if (c == 1):
                display.pixel(x + 75, y + 0, c)

    return 0


def print_display (display, l1, l2):
    bin_l1 = decide(l1)
    bin_l2 = decide(l2)

    display.fill(0) # Clear the display

    for y, row in enumerate(bin_l1):
        for x, c in enumerate(row):
            if (c == 1):
                display.pixel(x - 5, y + 0, c)

    for y, row in enumerate(bin_l2):
        for x, c in enumerate(row):
            if (c == 1):
                display.pixel(x + 75, y + 0, c)

    return 0


def center (string):
    length = len(string)
    print ( "Length of string is " + str( len(string) ) )
    if (length == 10):
        return string
    elif (length == 9):
        return " " + string
    elif (length == 8):
        return " " + string + " "
    elif (length == 7):
        return "  " + string + " "
    elif (length == 6):
        return "  " + string + "  "
    elif (length == 5):
        return "   " + string + "  "
    elif (length == 4):
        return "   " + string + "   "
    elif (length == 3):
        return "    " + string + "   "
    elif (length == 2):
        return "    " + string + "    "
    elif (length == 1):
        return "     " + string + "    "
    elif (length == 0):
        return "     " + string + "     "

    
def get_btc_price ():

    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    print("Fetching json from", URL)
    response = requests.get(URL)
    a = response.json()
    btc_price = a['bitcoin']['usd']

    print('This is BTC price: ' + str(int(btc_price)))
    string = str(int(btc_price))
    return string

def get_eth_price ():

    URL = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"

    print("Fetching json from", URL)
    response = requests.get(URL)
    a = response.json()
    eth_price = a['ethereum']['usd']

    print('This is ETH price: ' + str(int(eth_price)))
    string = str(int(eth_price))
    return string

def get_ada_price ():

    URL = "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd"

    print("Fetching json from", URL)
    response = requests.get(URL)
    a = response.json()
    price = a['cardano']['usd']

    print('This is ADA price: ' + str(price))
    string = str(price)
    return string

def get_prague_time ():
    URL = "http://worldtimeapi.org/api/timezone/Europe/Prague"

    print("Fetching json from", URL)
    response = requests.get(URL)
    a = response.json()
    value = a['datetime']

    string = value[11:13] + value[14:16]
    print('This is DATE value: ' +  value[11:13] + "separator" +  value[14:16] )
    return string


    
sleep_time=5
while True:

    time_to_display ( get_prague_time() , ":" )
    time.sleep(sleep_time)

    string_to_display ( "$" + get_btc_price(), "" )
    time.sleep(sleep_time)

    string_to_display ( "$" + get_eth_price(), "" )
    time.sleep(sleep_time)

    string_to_display ( "$" + get_ada_price(), "" )
    time.sleep(sleep_time)



