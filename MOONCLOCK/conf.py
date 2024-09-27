conf = {
    'apps': [
        # {
        #     'name': 'auto_contrast',
        #     'latitude': '50.073611',
        #     'longitude': '14.435664',
        #     'contrast_after_sunrise': 100,  # value from 0 to 255
        #     'contrast_after_sunset': 0,  # value from 0 to 255
        # },
        {
            'name': 'crypto',
            'api': 'binance',  # Change this to use Binance API
            'ticker': 'BTCUSDT',  # Use Binance ticker format
            'duration': 300
        },
        # {
        #     'name': 'time',
        #     'timezone': 'Europe/Prague',
        #     'duration': 600,
        #     'update_frequency': 0,
        # }
    ],
}

