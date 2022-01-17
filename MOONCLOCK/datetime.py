from adafruit_datetime import *

__tz_cache = {}


class RTC:

    def __init__(self, requests):
        self.requests = requests

        self.__load_time = None
        self.__datetime = None

    @property
    def datetime(self):
        import time
        if not self.__datetime:
            dt = datetime.fromisoformat(
                self.requests.get('http://worldtimeapi.org/api/timezone/Etc/UTC').json()['datetime'])
            self.__load_time = time.monotonic()
            self.__datetime = datetime.fromtimestamp(dt.timestamp()) + dt.utcoffset()

        return (self.__datetime + timedelta(seconds=time.monotonic() - self.__load_time)).timetuple()


class datetime(datetime):
    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        return cls._fromtimestamp(timestamp, False, tz)


def tz(requests, tzname):
    if not tzname in __tz_cache:
        offset = requests.get('http://worldtimeapi.org/api/timezone/{}'.format(tzname)).json()['raw_offset']

        class dynamictimezone(timezone):

            def __new__(cls):
                return super().__new__(cls, timedelta(seconds=offset), name=tzname)

        __tz_cache[tzname] = dynamictimezone()

    return __tz_cache[tzname]
