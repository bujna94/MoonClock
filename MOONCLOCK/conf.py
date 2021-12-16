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
        'update_frequency': 0,
    }, {
        'name': 'auto_contrast',
        'latitude': '50.073611',
        'longitude': '14.435664',
        'contrast_after_sunrise': 100,  # value from 0 to 255
        'contrast_after_sunset': 0,  # value from 0 to 255
    }],
}
