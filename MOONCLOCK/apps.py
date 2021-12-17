import time

from adafruit_datetime import datetime
from display import str_rjust


def get_current_datetime(requests, timezone):
    URL = 'http://worldtimeapi.org/api/timezone/' + timezone

    try:
        response = requests.get(URL)
    except:
        print('Cannot get current time from {}'.format(URL))
        return

    data = response.json()

    return datetime.fromisoformat(data['datetime'])


def timestamp_to_time(timestamp):
    hours = int(timestamp % 86400 // 60 // 60)
    minutes = int((timestamp % 86400 // 60) % 60)
    seconds = int(timestamp % 60)
    return hours, minutes, seconds


class App:
    def __init__(self, display_group, requests, duration=0, update_frequency=None):
        self.display_group = display_group
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

        datetime = get_current_datetime(self.requests, timezone)

        self.unixtime = datetime.timestamp() + datetime.utcoffset().seconds
        self.start = time.monotonic()
        self._last_hours = None
        self._last_minutes = None
        self._last_seconds = None

    def update(self, first):
        loop_start = time.monotonic()
        delta = time.monotonic() - self.start
        current_timestamp = self.unixtime + int(delta)

        hours, minutes, seconds = timestamp_to_time(current_timestamp)

        if not self.show_seconds and hours == self._last_hours and minutes == self._last_minutes:
            time.sleep(60 - seconds)  # Wait for the next minute
            return

        if self.show_seconds:
            string = '{}  {}  {}'.format(
                str_rjust(str(hours), 2, '0'), str_rjust(str(minutes), 2, '0'), str_rjust(str(seconds), 2, '0'))
        else:
            string = '{}  {}'.format(
                str_rjust(str(hours), 2, '0'), str_rjust(str(minutes), 2, '0'))

        print('This is current time: {}:{}:{}'.format(hours, minutes, seconds))

        if first:
            self._last_hours = None
            self._last_minutes = None
            self._last_seconds = None

            self.display_group.clear()

            if self.show_seconds:
                self.display_group.displays[1].render_character(':')
                self.display_group.displays[3].render_character(':')
            else:
                self.display_group.displays[2].render_character(':')
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

        self.display_group.clear()
        self.display_group.render_string(
            '{0}{1}{2}'.format(
                self.BASE_CURRENCY_CHARACTER_MAP.get(self.base_currency, ' '),
                str_rjust(str_price, 7),
                self.CRYPTO_CHARACTER_MAP.get(self.crypto, ' ') + ' '
            ),
            center=True, empty_as_transparent=True
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

    def update(self, first):
        URL = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&formatted=0'.format(
            self.latitude, self.longitude)

        try:
            response = self.requests.get(URL)
        except:
            return
        data = response.json()['results']

        # sr - sunrise
        # ss - sunset
        # c - current

        sr_datetime = datetime.fromisoformat(data['sunrise'])
        ss_datetime = datetime.fromisoformat(data['sunset'])
        c_datetime = get_current_datetime(self.requests, self.timezone)

        if ss_datetime <= c_datetime:
            self.display_group.contrast(self.contrast_after_sunset)
            print('updating contrast after sunset')
        elif sr_datetime <= c_datetime:
            self.display_group.contrast(self.contrast_after_sunrise)
            print('updating contrast after sunrise')
