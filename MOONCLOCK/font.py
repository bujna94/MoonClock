import symbols

SYMBOL_MAP = {
    '0': symbols.ZERO,
    '1': symbols.ONE,
    '2': symbols.TWO,
    '3': symbols.THREE,
    '4': symbols.FOUR,
    '5': symbols.FIVE,
    '6': symbols.SIX,
    '7': symbols.SEVEN,
    '8': symbols.EIGHT,
    '9': symbols.NINE,
    '.': symbols.DOT,
    '$': symbols.LARGEDOLLAR,
    '€': symbols.EURO,
    ':': symbols.LARGECOLON,
    'B': symbols.BTC,
    'E': symbols.ETH,
    'L': symbols.LTC,
    'D': symbols.DOGE,
    'A': symbols.ADA,
    'P': symbols.POLKADOT,
    'G': symbols.ALGORAND,
}


def get_symbol_for_character(character):

    try:
        return SYMBOL_MAP[character]
    except KeyError:
        return symbols.EMPTY
