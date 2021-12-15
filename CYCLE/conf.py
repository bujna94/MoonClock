# copy this configuration below this comment section and define your currencies, time, sleep time etc.
# you can find more details of the supported cryptocurrencies at https://www.coingecko.com/en/api/documentation

# as prefix and (or) postfix you can use cryptocurrency or currecly logo. Currently supported logos:
# Crypto
# B = Bitcoin
# E = Ethereum
# L = Litecoin
# D = Dogecoin
# A = Cardano
# P = Polkadot

# Currencies
# $ = dollar
# € = euro

# name = name of a cryptocurrenc. you can find this information here: https://www.coingecko.com/en/api/documentation but it's really intuitive
# value = enter in which fiat currecny you want to get the price. for time, enter your timezone 
# prefix = empty string or shortcut for a logo, fiat currency defined above
# postfix = empty string or shortcut for a logo, fiat currency defined above
# remove_decimal = 1 or 0, if 1 - removes decimals
# sleep_time = enter value in seconds that you want to have the cryptocurrency price or time displayed

# copy & paste as many lines in conf[] array as you want. No limitation for number of cryptocurrecties but you can only use logos that are defined above.
# conf = [
#        {'name' : 'bitcoin',    'value' : 'usd',            'prefix' : '$', 'postfix':'B',   'remove_decimal': 1, 'sleep_time' : 30 },
#        {'name' : 'ethereum',   'value' : 'eur',            'prefix' : 'E',  'postfix':'€',  'remove_decimal': 1, 'sleep_time' : 30 },
#        {'name' : 'polkadot',   'value' : 'eur',            'prefix' : '',  'postfix':'€',  'remove_decimal': 0, 'sleep_time' : 30 },
#        {'name' : 'time',       'value' : 'Europe/Prague',  'prefix' : '',  'postfix':'',   'remove_decimal': 0, 'sleep_time' : 30 },
# ]


conf = [
    {'name': 'bitcoin', 'value': 'usd', 'prefix': '$', 'postfix': 'B', 'remove_decimal': 1, 'sleep_time': 300},
    {'name': 'time', 'value': 'Europe/Prague', 'prefix': '', 'postfix': '', 'remove_decimal': 0, 'sleep_time': 300},
]
