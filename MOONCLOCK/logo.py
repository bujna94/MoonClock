import font

# Keys has to be lowercase!
LOGOS_MAP = {
    # Fiat logos
    'eur': '€',
    'eurt': '€',
    'gbp': '£',
    'usd': '$',
    'usdt': '$',
    'usdc': '$',
    'busd': '$',
    'ust': '$',
    'dai': '$',
    'tusd': '$',

    # Crypto logos
    'ada': font.CHAR_ADA,
    'cardano': font.CHAR_ADA,

    'baked': font.CHAR_BAKED,
    'baked-token': font.CHAR_BAKED,

    'btc': font.CHAR_BTC,
    'bitcoin': font.CHAR_BTC,

    'sat': font.CHAR_WIDESATOSHI,
    'sats': font.CHAR_WIDESATOSHI,
    'satoshi': font.CHAR_WIDESATOSHI,

    'doge': font.CHAR_DOGE,
    'dogecoin': font.CHAR_DOGE,

    'eth': font.CHAR_ETH,
    'ethereum': font.CHAR_ETH,

    'ltc': font.CHAR_LTC,
    'litecoin': font.CHAR_LTC,

    'dot': font.CHAR_POLKADOT,
    'polkadot': font.CHAR_POLKADOT,

    'ksm': font.CHAR_KSM,
    'kusama': font.CHAR_KSM,

    'rune': font.CHAR_THORCHAIN,
    'thorchain': font.CHAR_THORCHAIN,

    'vra': font.CHAR_VERASITY,
    'verasity': font.CHAR_VERASITY,

    'algo': font.CHAR_ALGORAND,
    'algorand': font.CHAR_ALGORAND,
}


def get_logo(name, default=' '):
    return LOGOS_MAP.get(name, default)


def get_logos(full_ticker):
    first_logo = None
    second_logo = None

    for logo_name in LOGOS_MAP.keys():
        if full_ticker.find(logo_name) == 0:
            first_logo = get_logo(logo_name)
        elif full_ticker.find(logo_name) > 0:
            second_logo = get_logo(logo_name)

    return first_logo, second_logo
