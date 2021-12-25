import ssl
import traceback

import adafruit_requests
import adafruit_tca9548a
import board
import busio
import socketpool
import wifi
import supervisor

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

i2c = busio.I2C(SCL, SDA, frequency=1400000)

if i2c.try_lock():
    print('i2c.scan():' + str(i2c.scan()))
    i2c.unlock()

tca = adafruit_tca9548a.TCA9548A(i2c)
display_group = DisplayGroup([BetterSSD1306_I2C(WIDTH, HEIGHT, tca[i]) for i in range(5)])

print('My MAC addr:', [hex(i) for i in wifi.radio.mac_address])
# try to connect to any wifi from the secrets.py file
connected = False
wifi_networks_available = wifi.radio.start_scanning_networks()
print('Available WiFi networks:')
for network in wifi_networks_available:
    print('\t{}\t\tRSSI: {}\tChannel: {}'.format(str(network.ssid, 'utf-8'), network.rssi, network.channel))
wifi.radio.stop_scanning_networks()

display_group.render_string('wifi setup', center=True)
display_group.show()
time.sleep(5)

while not connected:
    fail_count = 0
    for wifi_conf in secrets:
        try:
            print('Connecting to {}'.format(wifi_conf['ssid']))
            display_group.clear()
            display_group.render_string('{0} {1}'.format(font.CHAR_WIFI, wifi_conf['ssid'][:8]), center=False)
            display_group.show()
            time.sleep(1)
            wifi.radio.connect(wifi_conf['ssid'], wifi_conf['password'])
            print('Connected to {}!'.format(wifi_conf['ssid']))
            print('My IP address is', wifi.radio.ipv4_address)
            display_group.clear()
            display_group.render_string('{0} '.format(font.CHAR_CHECK), center=True)
            display_group.show()
            time.sleep(1)
            connected = True
            break
        except ConnectionError:
            fail_count += 1
            print('Connection to {} has failed. Trying next ssid...'.format(wifi_conf['ssid']))
            display_group.clear()
            display_group.render_string('{0} '.format(font.CHAR_CROSS), center=True)
            display_group.show()
            time.sleep(1)

    if fail_count == len(secrets):
        display_group.clear()
        display_group.render_string('no wifi!', center=True)
        display_group.show()
        time.sleep(5)
        display_group.clear()
        display_group.render_string('scanning..', center=True)
        display_group.show()
        time.sleep(5)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

APPS = {
    'auto_contrast': AutoContrastApp,
    'crypto': CryptoApp,
    'time': TimeApp,
    'blockheight': BlockHeight,
    'halving': Halving,
    'fees': Fees,
    'text': Text,
    'marketcap': MarketCap,
}


def main():
    apps = []

    # Initialize all apps
    for app_conf in conf['apps']:
        name = app_conf.pop('name')

        try:
            apps.append(APPS[name](display_group, requests, **app_conf))
        except KeyError:
            raise ValueError('Unknown app {}'.format(name))
        except:
            print('Initialization of application {} has failed'.format(APPS[name].__name__))

    # Run apps
    while True:
        for app in apps:
            try:
                app.run()
            except Exception as e:
                print('Application {} has crashed'.format(app.__class__.__name__))
                traceback.print_exception(type(e), e, e.__traceback__)
                time.sleep(1)
                supervisor.reload()


if __name__ == '__main__':
    main()
