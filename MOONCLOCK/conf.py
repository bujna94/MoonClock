# copy this configuration below this comment section and define your currencies, time, sleep time etc.
# you can find more details of the supported cryptocurrencies at https://www.coingecko.com/en/api/documentation

conf = {
    'apps': [
        {
            'name': 'moscow_time',
            'duration': 20,
            'update_frequency': 1,
            'duration': 60,
        },
        {
            'name': 'temperature',
            'city': 'Bystročice',
            'key': '6b7b8e55f551111371cd23d75872de5f',
            'units': 'metric',
            'duration': 10,
            'update_frequency': 15,
        },
        {
            'name': 'marketcap',
            'crypto': 'bitcoin',
            'base_currency': 'usd',
            'update_frequency': 1,
            'duration': 10,
        },
        {
            'name': 'difficulty',
            'duration': 10,
        },
        {
            'name': 'auto_contrast',
            'latitude': '50.073611',
            'longitude': '14.435664',
            'contrast_after_sunrise': 255,  # value from 0 to 255
            'contrast_after_sunset': 100,  # value from 0 to 255
        },
        {
            'name': 'crypto',
            'crypto': 'bitcoin',
            'base_currency': 'usd',
            'update_frequency': 1,
            'duration': 10,
        },
        {
            'name': 'time',
            'show_seconds': 1,
            'duration': 10,
        },
        {
            'name': 'fees',
            'update_frequency': 1,
            'duration': 10,
        },
        {
            'name': 'blockheight',
            'update_frequency': 1,
            'duration': 10,
        },
        {
            'name': 'halving',
            'update_frequency': 1,
            'duration': 10,
        },
    ],
}
