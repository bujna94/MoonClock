import time

from display import str_rjust


class App:
    def __init__(self, displays, requests, duration=60, update_frequency=None):
        self.displays = displays
        self.requests = requests
        self.duration = duration
        self.update_frequency = update_frequency if update_frequency else self.duration

    def run(self):
        total_duration = 0
        while True:
            start = time.monotonic()
            self.update()
            duration = time.monotonic() - start

            total_duration += duration
            sleep = self.update_frequency - duration

            if sleep > 0:
                time.sleep(sleep)

            if total_duration >= self.duration:
                break

    def update(self):
        raise NotImplementedError('You have to implement `run` method')


class TimeApp(App):
    def __init__(self, *args, timezone='Europe/Prague', **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone

    def update(self):
        URL = 'http://worldtimeapi.org/api/timezone/' + self.timezone

        try:
            response = self.requests.get(URL)
        except:
            print('Something went wrong')
            return

        datetime = response.json()['datetime']

        string = datetime[11:13] + ': ' + datetime[14:16]

        self.displays.clear()
        self.displays.render_string(string, center=True)
        self.displays.show()


class CryptoApp(App):
    CRYPTO_CHARACTER_MAP = {
        'bitcoin': 'B',
        'ethereum': 'E',
        'litecoin': 'L',
        'dogecoin': 'D',
        'cardano': 'A',
        'polkadot': 'P',
    }

    BASE_CURRENCY_CHARACTER_MAP = {
        'usd': '$',
        'eur': '€',
    }

    def __init__(self, *args, base_currency='usd', crypto='bitcoin', **kwargs):
        super().__init__(*args, **kwargs)
        self.base_currency = base_currency
        self.crypto = crypto

    def update(self):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids=' + self.crypto + '&vs_currencies=' + self.base_currency
        try:
            response = self.requests.get(URL)
        except:
            print('Something went wrong')
            return

        price = response.json()[self.crypto][self.base_currency]

        str_price = str(int(price) if price > 100 else price)

        print('This is ' + self.crypto + ' price: ' + str_price)

        self.displays.clear()
        self.displays.render_string(
            '{0}{1}{2}'.format(
                self.BASE_CURRENCY_CHARACTER_MAP.get(self.base_currency, ' '),
                str_rjust(str_price, 7),
                self.CRYPTO_CHARACTER_MAP.get(self.crypto, ' ') + ' '
            ),
            center=True, empty_as_transparent=True
        )
        self.displays.show()
