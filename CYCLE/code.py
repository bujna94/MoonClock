import ipaddress
import ssl

import adafruit_requests
import adafruit_tca9548a
import board
import busio
import socketpool
import wifi

from apps import *
from display import BetterSSD1306_I2C, DisplayGroup, str_rjust

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print('WiFi secrets are kept in secrets.py, please add them there!')
    raise

# Get configuration from a conf.py file
try:
    from conf import conf
except ImportError:
    print('No configuration found in conf.py, please add them there!')
    raise

WIDTH = 128
HEIGHT = 64

SDA = board.IO10
SCL = board.IO11

i2c = busio.I2C(SCL, SDA)

if i2c.try_lock():
    print('i2c.scan(): ' + str(i2c.scan()))
    i2c.unlock()

tca = adafruit_tca9548a.TCA9548A(i2c)
displays = DisplayGroup([BetterSSD1306_I2C(WIDTH, HEIGHT, tca[i]) for i in range(5)])

print('ESP32-S2 WebClient Test')

print('My MAC addr:', [hex(i) for i in wifi.radio.mac_address])

print('Available WiFi networks:')
for network in wifi.radio.start_scanning_networks():
    print('\t%s\t\tRSSI: %d\tChannel: %d' % (str(network.ssid, 'utf-8'),
                                             network.rssi, network.channel))
wifi.radio.stop_scanning_networks()

print('Connecting to %s' % secrets['ssid'])
wifi.radio.connect(secrets['ssid'], secrets['password'])
print('Connected to %s!' % secrets['ssid'])
print('My IP address is', wifi.radio.ipv4_address)

ipv4 = ipaddress.ip_address('8.8.4.4')
try:
    print('Ping google.com: %f ms' % (wifi.radio.ping(ipv4) * 1000))
except:
    print('Cannot ping google.com')

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


# main cycle of cryptocurrencies
while True:
    apps = []

    # Initialize all apps
    for dictionary in conf:
        name = str(dictionary['name'])
        value = str(dictionary['value'])
        decimal = dictionary['remove_decimal']
        prefix = str(dictionary['prefix'])
        postfix = str(dictionary['postfix'])
        sleep_time = dictionary['sleep_time']

        if name == 'time':
            apps.append(TimeApp(value, requests, displays, duration=sleep_time, update_frequency=30))
        else:
            apps.append(CryptoApp(value, name, requests, displays, duration=sleep_time))

    # Run apps
    for app in apps:
        app.run()
