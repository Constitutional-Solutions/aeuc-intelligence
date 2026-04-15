# base_144k.py

# Base-144k glyph system implementation

# Constants for base-144k
BASE_144K_CONSTANTS = {
    'A': 0,  'B': 1,  'C': 2,  'D': 3,
    'E': 4,  'F': 5,  'G': 6,  'H': 7,
    'I': 8,  'J': 9,  'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25, '0': 26, '1': 27,
    '2': 28, '3': 29, '4': 30, '5': 31,
    '6': 32, '7': 33, '8': 34, '9': 35,
    '!': 36, '@': 37, '#': 38, '$': 39,
    '%': 40, '^': 41, '&': 42, '*': 43,
    '(': 44, ')': 45, '-': 46, '_': 47,
    '=': 48, '+': 49, '{': 50, '}': 51,
    '[': 52, ']': 53, ':': 54, ';': 55,
    '\': 56, '"': 57, '\' : 58, '<': 59,
    '>': 60, ',': 61, '.': 62, '?': 63
}

# Glyph Encoding

def encode_glyph(glyph):
    return BASE_144K_CONSTANTS.get(glyph, -1)  # Return -1 for unknown glyphs

# Glyph Decoding

def decode_glyph(value):
    for glyph, val in BASE_144K_CONSTANTS.items():
        if val == value:
            return glyph
    return None  # Return None for unknown values
