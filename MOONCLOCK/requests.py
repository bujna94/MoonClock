import time

from adafruit_requests import *


class Session(Session):

    def request(self, *args, max_retry_count=5, sleep_between_retries=5, **kwargs):
        kwargs['timeout'] = kwargs.get('timeout', 30)

        retry_i = 0
        while retry_i < max_retry_count:
            retry_i += 1
            try:
                return super().request(*args, **kwargs)
            except RuntimeError as e:
                print(e)
                if retry_i == max_retry_count:
                    raise

                time.sleep(sleep_between_retries)
