from adafruit_datetime import datetime


def get_current_datetime(requests, timezone):
    url = 'http://worldtimeapi.org/api/timezone/' + timezone
    return datetime.fromisoformat(requests.get(url).json()['datetime'])


def timestamp_to_time(timestamp):
    hours = int(timestamp % 86400 // 60 // 60)
    minutes = int((timestamp % 86400 // 60) % 60)
    seconds = int(timestamp % 60)
    return hours, minutes, seconds


def center_string(string, capacity=10):
    length = len(string)
    margin = (capacity - length) // 2
    if margin < 0:
        margin = 0

    string = (' ' * margin) + string + (' ' * margin)

    if len(string) < capacity:
        string = (' ' * (capacity - len(string))) + string

    return string


def str_rjust(string, length, char=' '):
    while len(string) < length:
        string = char + string

    return string
