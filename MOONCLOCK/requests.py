import time

from adafruit_requests import *


class Session(Session):

    def request(self, *args, max_retry_count=5, sleep_between_retries=5, **kwargs):
        print('sending request:', args, kwargs)
        kwargs['timeout'] = kwargs.get('timeout', 30)

        retry_i = 0
        while retry_i < max_retry_count:
            retry_i += 1
            try:
                return super().request(*args, **kwargs)
            except Exception as e:
                print('request exception:', e)
                if retry_i == max_retry_count:
                    raise
                else:
                    print('Retrying request...')

                time.sleep(sleep_between_retries)
