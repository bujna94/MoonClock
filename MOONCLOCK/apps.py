import font
import time

from datetime import datetime, tz, timedelta
from utils import str_rjust, str_align, number_to_human


class App:
    def __init__(self, display_group, requests, align='right', duration=30, update_frequency=None):
        self.display_group = display_group
        self.requests = requests
        self.duration = duration
        self.align = align
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def run(self):
        used_duration = 0
        while True:
            start = time.monotonic()
            self.update(
                first=(used_duration == 0),
                remaining_duration=self.duration - used_duration
            )
            update_duration = time.monotonic() - start

            sleep = self.update_frequency - update_duration

            if sleep > 0:
                time.sleep(sleep)

            used_duration += time.monotonic() - start
            if used_duration >= self.duration:
                break

    def update(self, first, remaining_duration):
        raise NotImplementedError('You have to implement `update` method')


class TimeApp(App):
    def __init__(self, *args, timezone='Europe/Prague', show_seconds=False, align='center', **kwargs):
        kwargs['update_frequency'] = 0
        super().__init__(*args, **kwargs)
        self.timezone = timezone
        self.show_seconds = show_seconds
        self.align = align

        self.start = time.monotonic()
        self._last_hours = None
        self._last_minutes = None
        self._last_seconds = None

    def update(self, first, remaining_duration):
        loop_start = time.monotonic()
        now = datetime.now(tz(self.requests, self.timezone))

        if first:
            self._last_hours = None
            self._last_minutes = None
            self._last_seconds = None

        if not self.show_seconds and now.hour == self._last_hours and now.minute == self._last_minutes:
            sleep = 60 - now.second
            sleep = remaining_duration if sleep > remaining_duration else sleep
            time.sleep(sleep)  # Wait for the next minute
            return

        if self.show_seconds:
            string = '{}  {}  {}'.format(
                str_rjust(str(now.hour), 2, '0'), str_rjust(str(now.minute), 2, '0'),
                str_rjust(str(now.second), 2, '0'),
            )
        else:
            string = '{}  {}'.format(
                str_rjust(str(now.hour), 2, '0'), str_rjust(str(now.minute), 2, '0')
            )

        print('This is current time: {}:{}:{}'.format(now.hour, now.minute, now.second))

        if first:
            self.display_group.clear()

            if self.show_seconds:
                self.display_group.displays[1].render_character(font.CHAR_WIDECOLON)
                self.display_group.displays[3].render_character(font.CHAR_WIDECOLON)
            else:
                self.display_group.displays[2].render_character(font.CHAR_WIDECOLON)
            self.display_group.show()

        self.display_group.render_string(string, center=True)

        if self.show_seconds:
            if self._last_hours != now.hour:
                self.display_group.displays[0].show()
            if self._last_minutes != now.minute:
                self.display_group.displays[2].show()
            if self._last_seconds != now.second:
                self.display_group.displays[4].show()
        else:
            if self._last_hours != now.hour:
                self.display_group.displays[1].show()
            if self._last_minutes != now.minute:
                self.display_group.displays[3].show()
        sleep = 1 - (time.monotonic() - loop_start)

        if sleep > 0:
            time.sleep(sleep)

        self._last_hours = now.hour
        self._last_minutes = now.minute
        self._last_seconds = now.second


class CryptoApp(App):
    CRYPTO_CHARACTER_MAP = {
        'cardano': font.CHAR_ADA,
        'baked-token': font.CHAR_BAKED,
        'bitcoin': font.CHAR_BTC,
        'dogecoin': font.CHAR_DOGE,
        'ethereum': font.CHAR_ETH,
        'litecoin': font.CHAR_LTC,
        'polkadot': font.CHAR_POLKADOT,
        'kusama': font.CHAR_KSM,
        'thorchain': font.CHAR_THORCHAIN,
        'verasity': font.CHAR_VERASITY,
    }

    BASE_CURRENCY_CHARACTER_MAP = {
        'usd': '$',
        'eur': '€',
        'gbp': '£',
        'sats': font.CHAR_WIDESATOSHI,
        'btc': font.CHAR_BTC,
    }

    def __init__(self, *args, base_currency='usd', crypto='bitcoin', align='right', decimals=4, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_currency = base_currency
        self.crypto = crypto
        self.align = align
        self.decimals = decimals

    def update(self, first, remaining_duration):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}'.format(
            self.crypto, self.base_currency)

        price = self.requests.get(URL).json()[self.crypto][self.base_currency]
        str_price = str(int(price) if price > 100 else price)[:7]
        if price < 1:
            str_price = str(round(price, self.decimals))

        print('This is ' + self.crypto + ' price: ' + str_price)

        self.display_group.clear()
        self.display_group.render_string(
            '{0}{1}{2} '.format(
                self.BASE_CURRENCY_CHARACTER_MAP.get(self.base_currency, ' '),
                str_align(str_price, 7, ' ', self.align),
                self.CRYPTO_CHARACTER_MAP.get(self.crypto, ' ')
            ),
            center=True
        )
        self.display_group.show()


class AutoContrastApp(App):
    def __init__(self, *args, latitude=None, longitude=None, contrast_after_sunrise=None, contrast_after_sunset=None,
                 **kwargs):
        kwargs['duration'] = 0
        super().__init__(*args, **kwargs)

        self.latitude = latitude
        self.longitude = longitude
        self.contrast_after_sunrise = contrast_after_sunrise
        self.contrast_after_sunset = contrast_after_sunset

    def update(self, first, remaining_duration):
        url = 'http://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&formatted=0'.format(
            self.latitude, self.longitude)

        data = self.requests.get(url).json()['results']

        sunrise_datetime = datetime.fromisoformat(data['sunrise']).timestamp()
        sunset_datetime = datetime.fromisoformat(data['sunset']).timestamp()
        current_datetime = datetime.now().timestamp()

        if sunset_datetime <= current_datetime:
            self.display_group.contrast(self.contrast_after_sunset)
            print('changing contrast after sunset')
        elif sunrise_datetime <= current_datetime:
            self.display_group.contrast(self.contrast_after_sunrise)
            print('changing contrast after sunrise')


class BlockHeight(App):
    def __init__(self, *args, align='center', mempool_space_api='https://mempool.space', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.mempool_space_api = mempool_space_api

    def update(self, first, remaining_duration):
        URL = '{}/api/blocks/tip/height'.format(self.mempool_space_api)

        height = self.requests.get(URL).content.decode()
        str_height = str(height)

        print('This is current block height: ' + str_height)

        self.display_group.clear()
        self.display_group.render_string(
            '{} {}{}'.format(
                font.CHAR_CHAIN,
                str_align(str_height, 6, ' ', self.align),
                font.CHAR_BTC
            ), center=False
        )
        self.display_group.show()


class Halving(App):
    def __init__(self, *args, align='center', mempool_space_api='https://mempool.space', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.mempool_space_api = mempool_space_api

    def update(self, first, remaining_duration):
        URL = '{}/api/blocks/tip/height'.format(self.mempool_space_api)

        height = self.requests.get(URL).content.decode()
        halving = str(210000 - int(height) % 210000)

        print('Halving in: ' + halving)

        self.display_group.clear()
        self.display_group.render_string(
            '{0} {1}'.format(
                font.CHAR_HALVING,
                str_align(halving, 6, ' ', self.align),
            ), center=False
        )
        self.display_group.show()


class Fees(App):
    def __init__(self, *args, align='center', mempool_space_api='https://mempool.space', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.mempool_space_api = mempool_space_api

    def update(self, first, remaining_duration):
        URL = '{}/api/v1/fees/recommended'.format(self.mempool_space_api)
        fees = self.requests.get(URL).json()
        fastest_fee = str(fees['fastestFee'])
        hour_fee = str(fees['hourFee'])

        print('Recommended fees:', fastest_fee + ':' + hour_fee)

        if len(fastest_fee) + len(hour_fee) > 5:
            fee_string = '{}{}:{}{}'.format(font.CHAR_SATOSHI, fastest_fee, font.CHAR_SATOSHI, hour_fee)
            str_to_render = str_align(fee_string, 10, ' ', self.align)
        else:
            fee_string = '{}{}:{}{}'.format(font.CHAR_SATOSHI, fastest_fee, font.CHAR_SATOSHI, hour_fee)
            str_to_render = '{} {}'.format(font.CHAR_MONEY_BAG, str_align(fee_string, 7, ' ', self.align))

        self.display_group.clear()
        self.display_group.render_string(str_to_render, center=False)
        self.display_group.show()


class Text(App):
    def __init__(self, *args, text='', align='center', **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.align = align

    def update(self, first, remaining_duration):
        text = str(self.text)
        print('Show text: ', text)

        self.display_group.clear()
        self.display_group.render_string(str_align(text, 10, ' ', self.align), center=False)
        self.display_group.show()


class MarketCap(App):
    CRYPTO_CHARACTER_MAP = {
        'cardano': font.CHAR_ADA,
        'baked-token': font.CHAR_BAKED,
        'bitcoin': font.CHAR_BTC,
        'dogecoin': font.CHAR_DOGE,
        'ethereum': font.CHAR_ETH,
        'litecoin': font.CHAR_LTC,
        'polkadot': font.CHAR_POLKADOT,
        'kusama': font.CHAR_KSM,
    }

    BASE_CURRENCY_CHARACTER_MAP = {
        'usd': '$',
        'eur': '€',
        'gbp': '£',
        'sats': font.CHAR_WIDESATOSHI,
        'btc': font.CHAR_BTC,
    }

    def __init__(self, *args, crypto='bitcoin', base_currency='usd', align='center', **kwargs):
        super().__init__(*args, **kwargs)
        self.crypto = crypto
        self.base_currency = base_currency
        self.align = align

    def update(self, first, remaining_duration):
        URL = 'https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=true' \
              '&community_data=false&developer_data=false&sparkline=false'.format(self.crypto)

        market_cap = self.requests.get(URL).json()['market_data']['market_cap'][self.base_currency]

        market, market_letter = number_to_human(market_cap)

        str_market_cap = '{0}{1}'.format(str(round(float(market), 1)), str(market_letter))

        print('This is ' + self.crypto + ' market cap: ' + str_market_cap)

        self.display_group.clear()
        self.display_group.render_string(
            '{0}{1}{2} '.format(
                self.BASE_CURRENCY_CHARACTER_MAP.get(self.base_currency, ' '),
                str_align(str_market_cap, 7, ' ', self.align),
                self.CRYPTO_CHARACTER_MAP.get(self.crypto, ' ')
            ),
            center=True
        )
        self.display_group.show()


class MoscowTime(App):
    def __init__(self, *args, align='right', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align

    def update(self, first, remaining_duration):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        price = self.requests.get(URL).json()['bitcoin']['usd']
        price = 100000000 / price

        str_price = str(int(price))
        str_hour = str_price[:2]
        str_min = str_price[2:]

        print('This is Moscow Time' + ' : ' + str_hour + ':' + str_min)

        self.display_group.clear()
        self.display_group.render_string(
            str_align('{} {}{} {}{} '.format(font.CHAR_MOSCOW, str_hour, font.CHAR_WIDECOLON, str_min, font.CHAR_MOSCOW), 10, ' ', 'center'), center=False
        )
        self.display_group.show()


class Difficulty(App):
    def __init__(self, *args, align='center', mempool_space_api='https://mempool.space', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.mempool_space_api = mempool_space_api

    def update(self, first, remaining_duration):
        URL = '{}/api/v1/difficulty-adjustment'.format(self.mempool_space_api)

        difficulty_adjustment = str(round(float(self.requests.get(URL).json()['difficultyChange']), 1))

        self.display_group.clear()
        self.display_group.render_string(
            str_align('{}{}'.format(difficulty_adjustment, '%'), 10, ' ', self.align),
            center=True
        )
        self.display_group.show()


class Temperature(App):
    def __init__(self, *args, align='center', city=None, key=None, units=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.city = city
        self.key = key
        self.units = units
        if city is None or key is None or units is None:
            print('Not defined argument city:{} or key:{} or units:{}'.format(city, key[:5], units))
            raise ValueError('Not defined argument city:{} or key:{} or units:{}'.format(city, key, units))

    def update(self, first, remaining_duration):
        URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'.format(self.city, self.key, self.units)
        temp = str(round(float(self.requests.get(URL).json()['main']['temp']), 2))
        print ('Current temperature in ' + self.city + ' is ' + temp)
        self.display_group.clear()
        self.display_group.render_string(str_align('{}{}'.format(temp, '°C'), 8, ' ', self.align), center=True)
        self.display_group.show()

class TestDisplay(App):
    def __init__(self, *args, update_frequency=None, fill=1, duration=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.duration = duration
        self.fill = fill
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def update(self, first, remaining_duration):
        if self.fill == 1:
            self.display_group.fill()
        else:
            self.display_group.clear()
        self.display_group.show()


# EXPERIMENTAL!!!
class Xpub(App):
    def __init__(self, *args, align='center', xpub='', limit=10, offset=0, step_addresses=10, end_when_unused=100, btc_rpc_explorer_api='https://explorer.sats.cz', update_frequency=None, duration=1, waittime=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.duration = duration
        self.waittime = waittime
        self.xpub = xpub
        self.limit = limit
        self.offset = offset
        self.end_when_unused = end_when_unused
        self.step_addresses = step_addresses
        self.btc_rpc_explorer_api = btc_rpc_explorer_api
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def update(self, first, remaining_duration):
        balance_total = 0
        unused_addreses = 0
        local_offset = 0
        print ('Checking addresses...')
        while(True):
            URL = '{}/api/util/xyzpub/{}?limit={}&offset={}'.format(self.btc_rpc_explorer_api, self.xpub, self.step_addresses, local_offset)
            content = self.requests.get(URL).json()
            addresses = content['receiveAddresses'] + content['changeAddresses']
            for a in addresses:
                URL_a = '{}/api/address/{}'.format(self.btc_rpc_explorer_api, a)
                addr_content = self.requests.get(URL_a).json()
                address_txcount = addr_content['txHistory']['txCount']
                address_balance = addr_content['txHistory']['balanceSat']
                balance_total += address_balance
                if address_txcount == 0:
                    unused_addreses += 1
                else:
                    unused_addreses = 0
            local_offset += self.step_addresses
            if unused_addreses > self.end_when_unused:
                break
        (balance_human, ext_human) = number_to_human(balance_total)
        str_balance=str(round(float(balance_human), 2)) + str(ext_human)
        print ('Your current balance: ' + str_balance)
        self.display_group.clear()
        self.display_group.render_string(str_balance, center=True)
        self.display_group.show()
        time.sleep(self.duration + self.waittime)


class LnbitsWalletBalance(App):
    def __init__(self, *args, align='center', update_frequency=None, server='https://pay.sats.cz', invoicereadkey='', duration=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align
        self.duration = duration
        self.server = server
        self.invoicereadkey = invoicereadkey
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def update(self, first, remaining_duration):

        URL = '{}/api/v1/wallet'.format(self.server)
        try:
            content = self.requests.get(URL, headers={"X-Api-Key": self.invoicereadkey}).json()
            str_balance = str_align(str(content['balance'] // 1000), 10, ' ', self.align)
        except:
            str_balance = 'wrong key'

        print ('There is ' + str_balance + ' sats available on ' + self.invoicereadkey)

        self.display_group.clear()
        self.display_group.render_string(str_balance, center=False)
        self.display_group.show()
