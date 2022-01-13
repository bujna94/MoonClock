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
                self.requests.get('http://worldtimeapi.org/api/timezone/Etc/UTC', timeout=5).json()['datetime'])
            self.__load_time = time.monotonic()
            self.__datetime = datetime.fromtimestamp(dt.timestamp()) + dt.utcoffset()

        return (self.__datetime + timedelta(seconds=time.monotonic() - self.__load_time)).timetuple()


class datetime(datetime):
    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        return cls._fromtimestamp(timestamp, False, tz)


def tz(requests, timezone):
    if timezone not in __tz_cache:
        offset = requests.get('http://worldtimeapi.org/api/timezone/{}'.format(timezone), timeout=5).json()['raw_offset']

        class dynamictzinfo(tzinfo):
            _offset = timedelta(seconds=offset)

            def utcoffset(self, dt):
                return self._offset

            def tzname(self, dt):
                return timezone

        __tz_cache[timezone] = dynamictzinfo()

    return __tz_cache[timezone]
