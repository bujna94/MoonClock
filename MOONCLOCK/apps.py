import font
import time

from adafruit_datetime import datetime
from utils import get_current_datetime, timestamp_to_time, str_align


class App:
    def __init__(self, display_group, requests, duration=1, align='right', update_frequency=None):
        self.display_group = display_group
        self.requests = requests
        self.duration = duration
        self.align = align
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def run(self):
        used_duration = 0
        while True:
            start = time.monotonic()
            self.update(first=(used_duration == 0), remaining_duration=self.duration - used_duration)
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
    def __init__(self, *args, timezone='Europe/Prague', show_seconds=False, align = 'center', **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone
        self.show_seconds = show_seconds
        self.align = align

        datetime = get_current_datetime(self.requests, timezone)

        self.unixtime = datetime.timestamp() + datetime.utcoffset().seconds
        self.start = time.monotonic()
        self._last_hours = None
        self._last_minutes = None
        self._last_seconds = None

    def update(self, first, remaining_duration):
        loop_start = time.monotonic()
        delta = time.monotonic() - self.start
        current_timestamp = self.unixtime + int(delta)

        hours, minutes, seconds = timestamp_to_time(current_timestamp)

        if first:
            self._last_hours = None
            self._last_minutes = None
            self._last_seconds = None

        if not self.show_seconds and hours == self._last_hours and minutes == self._last_minutes:
            sleep = 60 - seconds
            sleep = remaining_duration if sleep > remaining_duration else sleep
            time.sleep(sleep)  # Wait for the next minute
            return

        if self.show_seconds:
            string = '{}  {}  {}'.format(
                str_align(str(hours), 2, '0', self.align), str_align(str(minutes), 2, '0', self.align), str_align(str(seconds), 2, '0', self.align))
        else:
            string = '{}  {}'.format(
                str_align(str(hours), 2, '0', self.align), str_align(str(minutes), 2, '0', self.align))

        print('This is current time: {}:{}:{}'.format(hours, minutes, seconds))

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
            if self._last_hours != hours:
                self.display_group.displays[0].show()
            if self._last_minutes != minutes:
                self.display_group.displays[2].show()
            if self._last_seconds != seconds:
                self.display_group.displays[4].show()
        else:
            if self._last_hours != hours:
                self.display_group.displays[1].show()
            if self._last_minutes != minutes:
                self.display_group.displays[3].show()
        sleep = 1 - (time.monotonic() - loop_start)

        if sleep > 0:
            time.sleep(sleep)

        self._last_hours = hours
        self._last_minutes = minutes
        self._last_seconds = seconds


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
    }

    BASE_CURRENCY_CHARACTER_MAP = {
        'usd': '$',
        'eur': '€',
        'gbp': '£',  
        'sats': font.CHAR_WIDESATOSHI,
        'btc': font.CHAR_BTC,
    }

    def __init__(self, *args, base_currency='usd', crypto='bitcoin', align = 'right', **kwargs):
        super().__init__(*args, **kwargs)
        self.base_currency = base_currency
        self.crypto = crypto
        self.align = align

    def update(self, first, remaining_duration):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}'.format(self.crypto, self.base_currency)

        price = self.requests.get(URL).json()[self.crypto][self.base_currency]
        str_price = str(int(price) if price > 100 else price)[:7]
        if price < 1:
            str_price = str(round(price, 4))

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
        super().__init__(*args, **kwargs)

        self.latitude = latitude
        self.longitude = longitude
        self.contrast_after_sunrise = contrast_after_sunrise
        self.contrast_after_sunset = contrast_after_sunset
        self.timezone = 'Etc/UTC'

    def update(self, first, remaining_duration):
        url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&formatted=0'.format(
            self.latitude, self.longitude)

        data = self.requests.get(url).json()['results']

        sunrise_datetime = datetime.fromisoformat(data['sunrise'])
        sunset_datetime = datetime.fromisoformat(data['sunset'])
        current_datetime = get_current_datetime(self.requests, self.timezone)

        if sunset_datetime <= current_datetime:
            self.display_group.contrast(self.contrast_after_sunset)
            print('changing contrast after sunset')
        elif sunrise_datetime <= current_datetime:
            self.display_group.contrast(self.contrast_after_sunrise)
            print('changing contrast after sunrise')


class BlockHeight(App):
    def __init__(self, *args, align = 'center', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align

    def update(self, first, remaining_duration):
        URL = 'https://mempool.space/api/blocks/tip/height'

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
    def __init__(self, *args, align = 'center', **kwargs):
        super().__init__(*args, **kwargs)
        self.align=align

    def update(self, first, remaining_duration):
        URL = 'https://mempool.space/api/blocks/tip/height'

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
    def __init__(self, *args, align = 'center', **kwargs):
        super().__init__(*args, **kwargs)
        self.align = align


    def update(self, first, remaining_duration):
        URL = 'https://mempool.space/api/v1/fees/recommended'
        fees = self.requests.get(URL).json()
        fastest_fee = str(fees['fastestFee'])
        hour_fee = str(fees['hourFee'])
        
        print('Recommended fees:', str(fees))
        
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
        URL = 'https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'.format(self.crypto)

        market_cap = self.requests.get(URL).json()['market_data']['market_cap'][self.base_currency]
        
        index=0
        arr = ['', 'k', 'M', 'B', 'T', 'Q']
        while market_cap >=1000:
            index=index+1
            market_cap /= 1000


        str_market_cap = '{0}{1}'.format(
            str(round(float(market_cap),1)),
            str(arr[index]),
        )

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
