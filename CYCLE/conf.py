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

conf = {
    'apps': [{
        'name': 'crypto',
        'base_currency': 'usd',
        'crypto': 'bitcoin',
        'duration': 60
    }, {
        'name': 'time',
        'timezone': 'bitcoin',
        'duration': 300,
        'update_frequency': 30,
    }],
}
