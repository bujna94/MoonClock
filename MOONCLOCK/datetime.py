from adafruit_datetime import *
from ntp import NTP

__tz_cache = {}


class RTC:

    def __init__(self, requests, socketpool):
        self.requests = requests
        self.socketpool = socketpool
        self.ntp = NTP(socketpool)

        self.__load_time = None
        self.__datetime = None

    @property
    def datetime(self):
        import time
        if not self.__datetime:
            self.__load_time = time.monotonic()
            self.__datetime = datetime.fromtimestamp(self.ntp.unixtime())

        return (self.__datetime + timedelta(seconds=time.monotonic() - self.__load_time)).timetuple()


class datetime(datetime):
    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        return cls._fromtimestamp(timestamp, False, tz)


def tz(requests, tzname):
    if tzname not in __tz_cache:
        offset = requests.get('https://www.timeapi.io/api/TimeZone/zone?timeZone={}'.format(tzname)).json()['currentUtcOffset']['seconds']

        class dynamictimezone(timezone):

            def __new__(cls):
                return super().__new__(cls, timedelta(seconds=offset), name=tzname)

        __tz_cache[tzname] = dynamictimezone()

    return __tz_cache[tzname]
