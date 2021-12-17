#!/usr/bin/env python3

import glob
import io
import math
import sys

from PIL import Image

if len(sys.argv) == 1:
    files = [sys.stdin.buffer]
else:
    files = [open(x, 'rb') for x in glob.glob(sys.argv[1])]

for f in files:
    img = Image.open(io.BytesIO(f.read()))
    pixels = img.load()
    symbol = []
    for i in range(img.size[1]):
        col = []
        for j in range(img.size[0]):
            col.append(round(pixels[j, i] / 255))
        symbol.append(col)

    out = [0 for _ in range(math.ceil(len(symbol) * len(symbol[0]) / 8))]
    for row_i in range(len(symbol)):
        for col_i in range(len(symbol[row_i])):
            out[(row_i // 8) * len(symbol[row_i]) + col_i] |= int(symbol[row_i][col_i]) << (row_i % 8)

    if f != sys.stdin.buffer:
        print(f"{f.name[:-4]} = (({len(symbol[0])}, {len(symbol)}), " + str(bytearray(out)) + ')')
        f.close()
    else:
        print(f"(({len(symbol[0])}, {len(symbol)}), " + str(bytearray(out)) + ')')
