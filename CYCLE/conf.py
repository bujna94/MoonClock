
#copy this configuration below this comment section and define your currencies, time, sleep time etc.
"""
conf = [
        {'name' : 'bitcoin',    'value' : 'usd',            'prefix' : '$', 'postfix':'',   'remove_decimal': 0, 'sleep_time' : 1 },
        {'name' : 'ethereum',   'value' : 'eur',            'prefix' : '',  'postfix':'€',  'remove_decimal': 1, 'sleep_time' : 1 },
        {'name' : 'polkadot',   'value' : 'eur',            'prefix' : '',  'postfix':'€',  'remove_decimal': 0, 'sleep_time' : 1 },
        {'name' : 'time',       'value' : 'Europe/Prague',  'prefix' : '',  'postfix':'',   'remove_decimal': 0, 'sleep_time' : 1 },
]

"""

conf = [
        {'name' : 'bitcoin',    'value' : 'usd',            'prefix' : '$', 'postfix':'',   'remove_decimal': 1, 'sleep_time' : 30 },
        {'name' : 'time',       'value' : 'Europe/Prague',  'prefix' : '',  'postfix':'',   'remove_decimal': 0, 'sleep_time' : 30 },
        {'name' : 'polkadot',   'value' : 'eur',            'prefix' : '',  'postfix':'€',  'remove_decimal': 0, 'sleep_time' : 1 },
]
