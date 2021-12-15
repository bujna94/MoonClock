import adafruit_ssd1306

from font import get_symbol_for_character


def center_string(string, capacity=10):
    length = len(string)
    margin = (capacity - length) // 2
    if margin < 0:
        margin = 0

    string = (' ' * margin) + string + (' ' * margin)

    if len(string) < capacity:
        string = (' ' * (capacity - len(string))) + string

    return string


def str_rjust(string, length, char=' '):
    while len(string) < length:
        string = char + string

    return string


class BetterSSD1306_I2C(adafruit_ssd1306.SSD1306_I2C):

    def render_character(self, character, x_offset=0):
        self.render_symbol(get_symbol_for_character(character), x_offset=x_offset)

    def render_symbol(self, symbol, x_offset=0):
        size = symbol[0]

        for i in range(len(symbol[1])):
            row = i // size[0]
            row_start_pos = row * self.width + 1
            row_end_pos = (row + 1) * self.width - 1 + 1
            index = row_start_pos + x_offset + (i % size[0])

            if row_start_pos <= index <= row_end_pos:
                self.buffer[index] = symbol[1][i]


class DisplayGroup:

    FIRST_CHARACTER_X_OFFSET = -5
    SECOND_CHARACTER_X_OFFSET = 75

    def __init__(self, displays):
        self.displays = displays

    def clear(self):
        for display in self.displays:
            display.fill(0)

    def render_string(self, string, center=False, empty_as_transparent=False):
        string = center_string(string) if center else string

        for i, character in enumerate(string):
            if i >= len(self.displays) * 2:
                break

            if character == ' ' and empty_as_transparent:
                continue

            display = self.displays[i // 2]
            if i % 2 == 0:
                display.render_character(character, self.FIRST_CHARACTER_X_OFFSET)
            else:
                display.render_character(character, self.SECOND_CHARACTER_X_OFFSET)

    def show(self):
        for display in self.displays:
            display.show()
