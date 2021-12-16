import ipaddress
import ssl

import adafruit_requests
import adafruit_tca9548a
import board
import busio
import socketpool
import wifi

from apps import *
from display import BetterSSD1306_I2C, DisplayGroup

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
    print('i2c.scan():' + str(i2c.scan()))
    i2c.unlock()

tca = adafruit_tca9548a.TCA9548A(i2c)
display_group = DisplayGroup([BetterSSD1306_I2C(WIDTH, HEIGHT, tca[i]) for i in range(5)])

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

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


def main():
    apps = []

    # Initialize all apps
    for app_conf in conf['apps']:
        name = app_conf.pop('name')

        if name == 'time':
            apps.append(TimeApp(display_group, requests, **app_conf))
        elif name == 'crypto':
            apps.append(CryptoApp(display_group, requests, **app_conf))
        else:
            raise ValueError('Unknown app {}'.format(name))

    # Run apps
    while True:
        for app in apps:
            app.run()


if __name__ == '__main__':
    main()
