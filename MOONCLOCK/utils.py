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
        index = index + 1
        number /= 1000
    return number, arr[index]
