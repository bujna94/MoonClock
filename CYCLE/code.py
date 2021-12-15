import ipaddress
import ssl
import time

import adafruit_requests
import adafruit_tca9548a
import board
import busio
import socketpool
import wifi

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


# formats time and shows it on displays

# get current time (hours, minutes)
def get_time(timezone):
    URL = 'http://worldtimeapi.org/api/timezone/' + timezone

    print('Fetching json from', URL)
    try:
        response = requests.get(URL)
    except:
        print('Something went wrong')
        return ''
    a = response.json()
    value = a['datetime']

    string = value[11:13] + ': ' + value[14:16]
    print('This is time value: ' + value[11:13] + ':' + value[14:16])
    return string


# accepts crypto ticker ('bitcoin', 'ethereum', 'cardano' ,'polkadot'), fiat currency and to_integer (if true, no decimals are shown).
def get_crypto_price(ticker, currency, to_integer):
    URL = 'https://api.coingecko.com/api/v3/simple/price?ids=' + ticker + '&vs_currencies=' + currency
    print('Fetching json from', URL)
    try:
        response = requests.get(URL)
    except:
        print('Something went wrong')
    a = response.json()
    price = a[ticker][currency]

    if (to_integer):
        price = int(price)

    value = str(price)

    print('This is ' + ticker + ' price: ' + value)
    return value


# main cycle of cryptocurrencies
while True:
    for dictionary in conf:
        name = str(dictionary['name'])
        value = str(dictionary['value'])
        decimal = dictionary['remove_decimal']
        prefix = str(dictionary['prefix'])
        postfix = str(dictionary['postfix'])

        if name == 'time':
            displays.clear()
            t = get_time(value)
            displays.render_string(t, center=True)
            displays.show()
        else:
            displays.clear()
            displays.render_string(
                '{0}{1}{2}'.format(prefix, str_rjust(get_crypto_price(name, value, decimal), 7), postfix + ' '),
                center=True, empty_as_transparent=True
            )
            displays.show()
        time.sleep(dictionary['sleep_time'])
