#!/usr/bin/env python3

import math
import sys

from PIL import Image, ImageFont, ImageDraw

if len(sys.argv) == 3:
    chars = sys.argv[2]
else:
    chars = '!#$%&+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz|~'
font_path = sys.argv[1]

ANCHOR = 'lb'
MAXHEIGHT_MULTIPLIERS = {
    '.': 0.2,
    ',': 0.2,
    '-': 0.2,
    '+': 0.2,
    '<': 0.5,
    '>': 0.5,
    ':': 0.7,
    '=': 0.5
}
CENTER_VERTICALLY = '+-:;<=>|~'
SIZE = (52, 64)
CHAR_NAMES = {
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE',
    '!': 'EXCLAMATION_MARK',
    '"': 'DOUBLE_QUOTE',
    '#': 'HASHMARK',
    '$': 'DOLLAR',
    '%': 'PERCENT',
    '&': 'AMPERSAND',
    '\'': 'SINGLE_QUOTE',
    '(': 'OPENING_BRACKET',
    ')': 'CLOSING_BRACKET',
    '*': 'MULTIPLICATION_SIGN',
    '+': 'PLUS_SIGN',
    ',': 'COMMA',
    '-': 'MINUS_SIGN',
    '.': 'DOT',
    '/': 'SLASH',
    ':': 'COLON',
    ';': 'SEMICOLON',
    '<': 'LEFT_ARROW',
    '>': 'RIGHT_ARROW',
    '\\': 'BACKSLASH',
    '[': 'OPENING_SQUARE_BRACKET',
    ']': 'CLOSING_SQUARE_BRACKET',
    '^': 'POWER_SIGN',
    '_': 'UNDERSCORE',
    '`': 'BACKTICK',
    '{': 'OPENING_SQUARE_BRACKET',
    '}': 'CLOSING_SQUARE_BRACKET',
    '|': 'VERTICAL_BAR',
    '~': 'TILDE',
    '@': 'AT_SIGN',
    '=': 'EQUAL_SIGN',
    '?': 'QUESTION_SIGN',
}


def detect_real_char_bbox(img):
    x0, y0, x1, y1 = img.size[0], img.size[1], 0, 0
    pixels = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixels[x, y] == 1 and x < x0:
                x0 = x

            if pixels[x, y] == 1 and y < y0:
                y0 = y

            if pixels[x, y] == 1 and x > x1:
                x1 = x

            if pixels[x, y] == 1 and y > y1:
                y1 = y

    return x0, y0, x1 + 1, y1 + 1

for ch in chars:
    font = None
    img = Image.new('1', SIZE)
    d = ImageDraw.Draw(img)
    pos = (0, SIZE[1])
    fontsize = 5
    font = ImageFont.truetype(font_path, fontsize)

    while True:
        img.paste(0, (0, 0, SIZE[0], SIZE[1]))
        d.text(pos, ch, font=font, fill=1, anchor=ANCHOR)

        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)

        # Center text horizontally
        dummybbox = d.textbbox(pos, ch, font=font, anchor=ANCHOR)
        width = dummybbox[2] - dummybbox[0]
        pos = ((SIZE[0] - width) / 2, SIZE[1])
        img.paste(0, (0, 0, SIZE[0], SIZE[1]))
        d.text(pos, ch, font=font, fill=1, anchor=ANCHOR)
        bbox = detect_real_char_bbox(img)
        leftmargin = bbox[0]
        rightmargin = SIZE[0] - bbox[2]
        if ch in CENTER_VERTICALLY:
            topmargin = bbox[1]
            bottommargin = SIZE[1] - bbox[3]
            pos = (pos[0] + math.floor((rightmargin - leftmargin) / 2), pos[1] + math.floor((bottommargin - topmargin) / 2))
        else:
            pos = (pos[0] + math.floor((rightmargin - leftmargin) / 2), SIZE[1])

        img.paste(0, (0, 0, SIZE[0], SIZE[1]))
        d.text(pos, ch, font=font, fill=1, anchor=ANCHOR)

        realbbox = detect_real_char_bbox(img)
        fakeimg = Image.new('1', (SIZE[0] * 2, SIZE[1]))
        faked = ImageDraw.Draw(fakeimg)
        faked.text((SIZE[0] / 2, pos[1]), ch, font=font, fill=1, anchor=ANCHOR)
        fakebbox = detect_real_char_bbox(fakeimg)
        if (realbbox[0] <= 0 and realbbox[2] >= SIZE[0]) or (realbbox[1] <= 0 and realbbox[3] >= SIZE[1]):
            break

        realwidth = realbbox[2] - realbbox[0]
        realheight = realbbox[3] - realbbox[1]
        fakewidth = fakebbox[2] - fakebbox[0]
        fakeheight = fakebbox[3] - fakebbox[1]

        if realheight >= SIZE[1] * MAXHEIGHT_MULTIPLIERS.get(ch, 1):
            break

        if realwidth < fakewidth or realheight < fakeheight:
            font = ImageFont.truetype(font_path, fontsize - 1)
            img.paste(0, (0, 0, SIZE[0], SIZE[1]))
            d.text(pos, ch, font=font, fill=1, anchor=ANCHOR)
            bbox = detect_real_char_bbox(img)
            leftmargin = bbox[0]
            rightmargin = SIZE[0] - bbox[2]
            if ch in CENTER_VERTICALLY:
                topmargin = bbox[1]
                bottommargin = SIZE[1] - bbox[3]
                pos = (pos[0] + math.floor((rightmargin - leftmargin) / 2), math.floor((bottommargin - topmargin) / 2))
            else:
                pos = (pos[0] + math.floor((rightmargin - leftmargin) / 2), SIZE[1])

            img.paste(0, (0, 0, SIZE[0], SIZE[1]))
            d.text(pos, ch, font=font, fill=1, anchor=ANCHOR)
            break

    filename = '{}.bmp'.format(CHAR_NAMES.get(ch, ch))
    print(filename)
    img.save(filename)
