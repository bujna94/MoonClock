from adafruit_datetime import datetime


def get_current_datetime(requests, timezone=''):
    url = ''
    if timezone:
        url = 'http://worldtimeapi.org/api/timezone/' + timezone
    else:
        url = 'http://worldtimeapi.org/api/ip'

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

def str_ljust(string, length, char=' '):
    while len(string) < length:
        string = string + char
    return string

def str_ljust(string, length, char=' '):
    while len(string) < length:
        string = string + char
    return string
    
def str_cjust(string, length, char=' '):
    while len(string) < length:
        string = char + string
        if len(string) < length:
            string = string + char
    return string


def str_align(string, length, char=' ', align='right'):
    if align == 'right':
        return str_rjust(string, length, char)
    elif align == 'left':
        return str_ljust(string, length, char)
    elif align == 'center':
        return str_cjust(string, length, char)
    else:
        raise ValueError('Unsupported alignment')


def number_to_human(number):
    arr = ['', 'k', 'M', 'B', 'T', 'Q']
    index = 0
    while number >= 1000:
        index = index+1
        number /= 1000
    return (number, arr[index])
