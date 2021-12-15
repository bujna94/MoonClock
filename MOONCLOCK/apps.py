import time

from display import str_rjust


class App:
    def __init__(self, displays, requests, duration=60, update_frequency=None):
        self.displays = displays
        self.requests = requests
        self.duration = duration
        self.update_frequency = update_frequency if update_frequency is not None else self.duration

    def run(self):
        total_duration = 0
        while True:
            start = time.monotonic()
            self.update(first=(total_duration == 0))
            duration = time.monotonic() - start

            sleep = self.update_frequency - duration

            if sleep > 0:
                time.sleep(sleep)

            total_duration += time.monotonic() - start
            if total_duration >= self.duration:
                break

    def update(self, first):
        raise NotImplementedError('You have to implement `update` method')


class TimeApp(App):
    def __init__(self, *args, timezone='Europe/Prague', show_seconds=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone
        self.show_seconds = show_seconds

        URL = 'http://worldtimeapi.org/api/timezone/' + self.timezone

        try:
            response = self.requests.get(URL)
        except:
            print('Cannot get current time from {}'.format(URL))
            return

        data = response.json()
        self.unixtime = data['unixtime'] + data['raw_offset']
        self.start = time.monotonic()
        self._last_hours = None
        self._last_minutes = None
        self._last_seconds = None

    def update(self, first):
        loop_start = time.monotonic()
        delta = time.monotonic() - self.start
        current_timestamp = self.unixtime + int(delta)

        hours = int(current_timestamp % 86400 // 60 // 60)
        minutes = int((current_timestamp % 86400 // 60) % 60)
        seconds = int(current_timestamp % 60)

        if not self.show_seconds and hours == self._last_hours and minutes == self._last_minutes:
            time.sleep(60 - seconds)  # Wait for the next minute
            return

        if self.show_seconds:
            string = '{}  {}  {}'.format(
                str_rjust(str(hours), 2, '0'), str_rjust(str(minutes), 2, '0'), str_rjust(str(seconds), 2, '0'))
        else:
            string = '{}  {}'.format(
                str_rjust(str(hours), 2, '0'), str_rjust(str(minutes), 2, '0'))

        if first:
            self._last_hours = None
            self._last_minutes = None
            self._last_seconds = None

            self.displays.clear()

            if self.show_seconds:
                self.displays.displays[1].render_character(':')
                self.displays.displays[3].render_character(':')
            else:
                self.displays.displays[2].render_character(':')
            self.displays.show()

        self.displays.render_string(string, center=True)

        if self.show_seconds:
            if self._last_hours != hours:
                self.displays.displays[0].show()
            if self._last_minutes != minutes:
                self.displays.displays[2].show()
            if self._last_seconds != seconds:
                self.displays.displays[4].show()
        else:
            if self._last_hours != hours:
                self.displays.displays[1].show()
            if self._last_minutes != minutes:
                self.displays.displays[3].show()
        sleep = 1 - (time.monotonic() - loop_start)

        if sleep > 0:
            time.sleep(sleep)

        self._last_hours = hours
        self._last_minutes = minutes
        self._last_seconds = seconds


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

    def update(self, first):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids=' + self.crypto + '&vs_currencies=' + self.base_currency
        try:
            response = self.requests.get(URL)
        except:
            print('Cannot get crypto price from {}'.format(URL))
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
