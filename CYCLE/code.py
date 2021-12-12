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


# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Get configuration from a conf.py file
try:
    from conf import conf
except ImportError:
    print("No configuration found in conf.py, please add them there!")
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
try:
    print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
except:
    print("Cannot ping google.com")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

#convert characters to binary representation
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
        return DOLLARLARGE
    elif number == str('€'):
        return EURO
    elif number == str(':'):
        return LARGECOLON
    elif number == str('B'):
        return BTC 
    elif number == str('E'):
        return ETH
    elif number == str('L'):
        return LTC
    elif number == str('D'):
        return DOGE
    elif number == str('A'):
        return ADA
    elif number == str('P'):
        return POLKADOT
    else:
        return EMPTY
        print ('this is empty or unsupported char')


#accepts string and shows it on displays
def string_to_display (string, prefix, postfix):
    centered_string = center ( string )
    print_logo (display1, prefix);
    print_display (display2, centered_string[0], centered_string[1]);
    print_display (display3, centered_string[2], centered_string[3]);
    print_display (display4, centered_string[4], centered_string[5]);
    print_logo (display5, postfix);
    display1.show()
    display2.show()
    display3.show()
    display4.show()
    display5.show()

#formats time and shows it on displays
def time_to_display (string, colon):
    centered_string = ("  " + string + "  ")
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


#accepts display, two numbers, colon_boolean. shows two numbers and colon in the center display if colon_boolean (third display) 
def print_time (display, l1, l2, colon_boolean):
    bin_l1 = decide(l1)
    bin_l2 = decide(l2)
    display.fill(0) # Clear the display

    if colon_boolean:
        for y, row in enumerate(LARGECOLON):
            for x, c in enumerate(row):
                c = int(c)
                if (c):
                    display.pixel(x + 0, y + 0, int(c))
    for y, row in enumerate(bin_l1):
        for x, c in enumerate(row):
            c = int(c)
            if (c):
                display.pixel(x - 5, y + 0, int(c))
    for y, row in enumerate(bin_l2):
        for x, c in enumerate(row):
            c = int(c)
            if (c):
                display.pixel(x + 75, y + 0, int(c))

def print_logo (display, logo):
    bin_logo = decide(logo)
    display.fill(0) # Clear the display

    for y, row in enumerate(bin_logo):
        for x, c in enumerate(row):
            display.pixel(x + 0, y + 0, int(c))
    
#accepts display nad two numbers to show from numbers.py
def print_display (display, l1, l2):
    bin_l1 = decide(l1)
    bin_l2 = decide(l2)

    display.fill(0) # Clear the display

    for y, row in enumerate(bin_l1):
        for x, c in enumerate(row):
            display.pixel(x - 5, y + 0, int(c))

    for y, row in enumerate(bin_l2):
        for x, c in enumerate(row):
            display.pixel(x + 75, y + 0, int(c))

#accepts any string and returns centered version, max length is 6, everything after 6th character is not considered. another 4 characters are locked for logo and currency
def center (string):
    length = len(string)
    if (length > 6):
        return string[0:6]
    elif (length == 6):
        return string
    elif (length == 5):
        return " " + string
    elif (length == 4):
        return " " + string + " "
    elif (length == 3):
        return "  " + string + " "
    elif (length == 3):
        return "  " + string + "  "
    elif (length == 2):
        return "   " + string + "  "
    elif (length == 1):
        return "   " + string + "   "
    elif (length == 0):
        return "    " + string + "   "

#get current time (hours, minutes)
def get_time (timezone):
    URL = "http://worldtimeapi.org/api/timezone/" + timezone

    print("Fetching json from", URL)
    try:
        response = requests.get(URL)
    except:
        print ("Something went wrong")
    a = response.json()
    value = a['datetime']

    string = value[11:13] + "  " + value[14:16]
    print('This is time value: ' +  value[11:13] + ":" +  value[14:16] )
    return string

#accepts crypto ticker ("bitcoin", "ethereum", "cardano" ,"polkadot"), fiat currency and to_integer (if true, no decimals are shown).
def get_crypto_price(ticker, currency, to_integer):
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=" + ticker + "&vs_currencies=" + currency
    print("Fetching json from", URL)
    try:
        response = requests.get(URL)
    except:
        print ("Something went wrong")
    a = response.json()
    price = a[ticker][currency]

    if (to_integer):
        price = int(price)

    value = str(price)

    print('This is ' + ticker + ' price: ' + value )
    return value

#main cycle of cryptocurrencies
while True:
    for dictionary in conf:
        name = str(dictionary['name'])
        value = str(dictionary['value'])
        decimal = dictionary['remove_decimal']
        prefix = str(dictionary['prefix'])
        postfix = str(dictionary['postfix'])
        if (name == "time"):
            time_to_display ( get_time( value ) , ":" )
        else:
            string_to_display ( get_crypto_price(name, value, decimal), prefix, postfix )
        time.sleep(dictionary['sleep_time'])










