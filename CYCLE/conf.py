
#copy this configuration below this comment section and define your currencies, time, sleep time etc.
#you can find more details of the supported cryptocurrencies at https://www.coingecko.com/en/api/documentation

#as prefix and (or) postfix you can use cryptocurrency or currecly logo. Currently supported logos:
# Crypto
# B = Bitcoin
# E = Ethereum
# L = Litecoin
# D = Dogecoin
# A = Cardano
# P = Polkadot
#  = 
#  = 

#Currencies
# $ = dollar
# € = euro

"""
conf = [
        {'name' : 'bitcoin',    'value' : 'usd',            'prefix' : '$', 'postfix':'B',   'remove_decimal': 0, 'sleep_time' : 30 },
        {'name' : 'ethereum',   'value' : 'eur',            'prefix' : 'E',  'postfix':'€',  'remove_decimal': 1, 'sleep_time' : 30 },
        {'name' : 'polkadot',   'value' : 'eur',            'prefix' : '',  'postfix':'€',  'remove_decimal': 0, 'sleep_time' : 30 },
        {'name' : 'time',       'value' : 'Europe/Prague',  'prefix' : '',  'postfix':'',   'remove_decimal': 0, 'sleep_time' : 30 },
]

"""

conf = [
        {'name' : 'bitcoin',    'value' : 'usd',            'prefix' : '$', 'postfix':'',   'remove_decimal': 1, 'sleep_time' : 30 },
        {'name' : 'time',       'value' : 'Europe/Prague',  'prefix' : '',  'postfix':'',   'remove_decimal': 0, 'sleep_time' : 30 },
]
