import symbols

# Unicode private use area starts from 0xE000
CHAR_ADA = '\ue000'
CHAR_BAKED = '\ue001'
CHAR_BTC = '\ue002'
CHAR_DOGE = '\ue003'
CHAR_ETH = '\ue004'
CHAR_LTC = '\ue005'
CHAR_POLKADOT = '\ue006'
CHAR_WIDECOLON = '\ue007'
CHAR_SATOSHI = '\ue008'

SYMBOLS_MAP = {
    ord('0'): symbols.ZERO,
    ord('1'): symbols.ONE,
    ord('2'): symbols.TWO,
    ord('3'): symbols.THREE,
    ord('4'): symbols.FOUR,
    ord('5'): symbols.FIVE,
    ord('6'): symbols.SIX,
    ord('7'): symbols.SEVEN,
    ord('8'): symbols.EIGHT,
    ord('9'): symbols.NINE,
    ord('.'): symbols.DOT,
    ord('$'): symbols.DOLLAR,
    ord('€'): symbols.EUR,
    ord('£'): symbols.GBP,
    ord(':'): symbols.COLON,
    ord(' '): symbols.EMPTY,
    ord('@'): symbols.AT,
    ord('°'): symbols.DEGREE,
    ord('÷'): symbols.DIVIDE,
    ord('='): symbols.EQUAL,
    ord('!'): symbols.EXCLAMATION_MARK,
    ord('#'): symbols.HASH,
    ord('-'): symbols.MINUS,
    ord('×'): symbols.MULTIPLY,
    ord('/'): symbols.OVER,
    ord('%'): symbols.PERCENT,
    ord('+'): symbols.PLUS,
    ord('?'): symbols.QUESTION_MARK,
    ord('*'): symbols.STAR,


    # Alphabet
    ord('A'): symbols.A,
    ord('B'): symbols.B,
    ord('C'): symbols.C,
    ord('D'): symbols.D,
    ord('E'): symbols.E,
    ord('F'): symbols.F,
    ord('G'): symbols.G,
    ord('H'): symbols.H,
    ord('I'): symbols.I,
    ord('J'): symbols.J,
    ord('K'): symbols.K,
    ord('L'): symbols.L,
    ord('M'): symbols.M,
    ord('N'): symbols.N,
    ord('O'): symbols.O,
    ord('P'): symbols.P,
    ord('Q'): symbols.Q,
    ord('R'): symbols.R,
    ord('S'): symbols.S,
    ord('T'): symbols.T,
    ord('U'): symbols.U,
    ord('V'): symbols.V,
    ord('W'): symbols.W,
    ord('X'): symbols.X,
    ord('Y'): symbols.Y,
    ord('Z'): symbols.Z,

    # Crypto logos
    ord(CHAR_ADA): symbols.ADA,
    ord(CHAR_BAKED): symbols.BAKED,
    ord(CHAR_BTC): symbols.BTC,
    ord(CHAR_DOGE): symbols.DOGE,
    ord(CHAR_ETH): symbols.ETH,
    ord(CHAR_LTC): symbols.LTC,
    ord(CHAR_POLKADOT): symbols.POLKADOT,
    ord(CHAR_WIDECOLON): symbols.WIDECOLON,
    ord(CHAR_SATOSHI): symbols.SATOSHI,
}


def get_symbol_for_character(character):

    try:
        return SYMBOLS_MAP[ord(character)]
    except KeyError:
        return symbols.EMPTY
