# copy this configuration below this comment section and define your currencies, time, sleep time etc.
# you can find more details of the supported cryptocurrencies at https://www.coingecko.com/en/api/documentation

conf = {
    'apps': [{
        'name': 'crypto',
        'base_currency': 'usd',
        'crypto': 'bitcoin',
        'duration': 60
    }, {
        'name': 'time',
        'timezone': 'Europe/Prague',
        'duration': 600,
        'update_frequency': 30,
    }],
}
