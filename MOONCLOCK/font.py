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
CHAR_KSM = '\ue009'
CHAR_CHAIN = '\ue00A'
CHAR_WIDESATOSHI = '\ue00B'
CHAR_MONEY_BAG = '\ue00C'
CHAR_HALVING = '\ue00D'
CHAR_WIFI = '\ue00E'
CHAR_CHECK = '\ue00F'
CHAR_CROSS = '\ue010'
CHAR_DELTA = '\ue011'
CHAR_SIGMA = '\ue012'
CHAR_MOSCOW = '\ue013'
CHAR_MONEY_BAG_SAT = '\ue014'
CHAR_THORCHAIN = '\ue015'
CHAR_VERASITY = '\ue016'
CHAR_ALGORAND = '\ue017'

SYMBOLS_MAP = {
    # Numbers
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
    ord('a'): symbols.A,
    ord('b'): symbols.B,
    ord('c'): symbols.C,
    ord('d'): symbols.D,
    ord('e'): symbols.E,
    ord('f'): symbols.F,
    ord('g'): symbols.G,
    ord('h'): symbols.H,
    ord('i'): symbols.I,
    ord('j'): symbols.J,
    ord('k'): symbols.K,
    ord('l'): symbols.L,
    ord('m'): symbols.M,
    ord('n'): symbols.N,
    ord('o'): symbols.O,
    ord('p'): symbols.P,
    ord('q'): symbols.Q,
    ord('r'): symbols.R,
    ord('s'): symbols.S,
    ord('t'): symbols.T,
    ord('u'): symbols.U,
    ord('v'): symbols.V,
    ord('w'): symbols.W,
    ord('x'): symbols.X,
    ord('y'): symbols.Y,
    ord('z'): symbols.Z,

    # Symbols
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
    ord('Δ'): symbols.DELTA,
    ord('Σ'): symbols.SIGMA,

    # Crypto logos
    ord(CHAR_ADA): symbols.ADA,
    ord(CHAR_BAKED): symbols.BAKED,
    ord(CHAR_BTC): symbols.BTC,
    ord(CHAR_DOGE): symbols.DOGE,
    ord(CHAR_ETH): symbols.ETH,
    ord(CHAR_LTC): symbols.LTC,
    ord(CHAR_POLKADOT): symbols.POLKADOT,
    ord(CHAR_KSM): symbols.KSM,
    ord(CHAR_THORCHAIN): symbols.THORCHAIN,
    ord(CHAR_VERASITY): symbols.VERASITY,
    ord(CHAR_ALGORAND): symbols.ALGORAND,

    # Other logos, characters
    ord(CHAR_WIDECOLON): symbols.WIDECOLON,
    ord(CHAR_SATOSHI): symbols.SATOSHI,
    ord(CHAR_WIDESATOSHI): symbols.WIDESATOSHI,
    ord(CHAR_CHAIN): symbols.CHAIN,
    ord(CHAR_MONEY_BAG): symbols.MONEY_BAG,
    ord(CHAR_MONEY_BAG_SAT): symbols.MONEY_BAG_SAT,
    ord(CHAR_HALVING): symbols.HALVING,
    ord(CHAR_WIFI): symbols.WIFI,
    ord(CHAR_DELTA): symbols.DELTA,
    ord(CHAR_SIGMA): symbols.SIGMA,
    ord(CHAR_MOSCOW): symbols.MOSCOW,
    ord(CHAR_CHECK): symbols.CHECK,
    ord(CHAR_CROSS): symbols.CROSS,
}


def get_symbol_for_character(character):

    try:
        return SYMBOLS_MAP[ord(character)]
    except KeyError:
        return symbols.EMPTY
