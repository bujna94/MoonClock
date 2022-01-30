import requests
import adafruit_tca9548a
import board
import busio
import json
import microcontroller
import rtc
import socketpool
import ssl
import time
import traceback
import wifi

from datetime import RTC

from apps import *
from display import BetterSSD1306_I2C, DisplayGroup


display_group = None


def reset():
    if display_group:
        try:
            display_group.render_string('RESET', center=True, empty_as_transparent=False)
            display_group.show()
        except Exception:
            pass

    print("Resetting....")
    time.sleep(30)
    microcontroller.on_next_reset(microcontroller.RunMode.NORMAL)
    microcontroller.reset()


# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print('WiFi secrets are kept in secrets.py, please add them there!')
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
display_group = DisplayGroup(
    [BetterSSD1306_I2C(WIDTH, HEIGHT, tca[i]) for i in range(5)])

print('My MAC addr:', [hex(i) for i in wifi.radio.mac_address])

display_group.render_string('wifi setup', center=True)
display_group.show()
time.sleep(1)

connected = False

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
        time.sleep(2)
        display_group.clear()
        display_group.render_string('scanning..', center=True)
        display_group.show()
        time.sleep(2)


# Get configuration from a conf.py file
try:
    with open('conf.json', 'r') as f:
        conf = json.loads(f.read())
except FileNotFoundError:
    # Backward compatibility
    try:
        from conf import conf
    except Exception as e:
        print(e)
        display_group.render_string('CONF ERROR')
        display_group.show()
        raise
except Exception as e:
    print(e)
    display_group.render_string('CONF ERROR')
    display_group.show()


pool = socketpool.SocketPool(wifi.radio)
requests_ = requests.Session(pool, ssl.create_default_context())

try:
    display_group.clear()
    display_group.render_string('TIME  INIT', center=True)
    display_group.show()
    rtc.set_time_source(RTC(requests_, pool))
except Exception as e:
    traceback.print_exception(type(e), e, e.__traceback__)
    reset()

APPS = {
    'auto_contrast': AutoContrastApp,
    'crypto': CryptoApp,
    'time': TimeApp,
    'blockheight': BlockHeight,
    'halving': Halving,
    'fees': Fees,
    'text': Text,
    'marketcap': MarketCap,
    'moscow_time': MoscowTime,
    'difficulty': Difficulty,
    'temperature': Temperature,
    'xpub': Xpub,
    'test': TestDisplay,
    'lnbits_wallet_balance': LnbitsWalletBalance,
}


def main():
    apps = []

    # Initialize all apps
    display_group.clear()
    display_group.render_string('APPS  INIT', center=True)
    display_group.show()
    for app_conf in conf['apps']:
        name = app_conf.pop('name')
        print('Initializing {} app'.format(name))

        try:
            apps.append(APPS[name](display_group, requests_, **app_conf))
        except KeyError:
            raise ValueError('Unknown app {}'.format(name))
        except Exception as e:
            print('Initialization of application {} has failed'.format(APPS[name].__name__))
            print(e)
            traceback.print_exception(type(e), e, e.__traceback__)

    # Run apps
    while True:
        for app in apps:
            try:
                print('Running {} app'.format(app.__class__.__name__))
                app.run()
            except Exception as e:
                print('Application {} has crashed'.format(app.__class__.__name__))
                print(e)
                traceback.print_exception(type(e), e, e.__traceback__)
                reset()


if __name__ == '__main__':
    main()
