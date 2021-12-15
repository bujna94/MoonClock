import time


from display import str_rjust


class App:
    def __init__(self, requests, displays, duration=60, update_frequency=None):
        self.requests = requests
        self.displays = displays
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
    def __init__(self, timezone='Europe/Prague', *args, **kwargs):
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
    def __init__(self, base='usd', crypto='bitcoin', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base = base
        self.crypto = crypto

    def update(self):
        URL = 'https://api.coingecko.com/api/v3/simple/price?ids=' + self.crypto + '&vs_currencies=' + self.base
        try:
            response = self.requests.get(URL)
        except:
            print('Something went wrong')
            return

        price = response.json()[self.crypto][self.base]

        if price >= 100:
            price = int(price)

        str_price = str(price)

        print('This is ' + self.crypto + ' price: ' + str_price)

        self.displays.clear()
        self.displays.render_string(
            '{0}{1}{2}'.format('$', str_rjust(str_price, 7), 'B '),
            center=True, empty_as_transparent=True
        )
        self.displays.show()
