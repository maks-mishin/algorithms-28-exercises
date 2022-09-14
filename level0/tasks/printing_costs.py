ascii_costs = {
    ' ': 0, '&': 24, ',': 7, '2': 22, '8': 23, '>': 10, 'D': 26,
    'J': 18, 'P': 23, 'V': 19, '\\': 10, 'b': 25, 'h': 21, 'n': 18,
    't': 17, 'z': 19, '!': 9, "'": 3, '-': 7, '3': 23, '9': 26,
    '?': 15, 'E': 26, 'K': 21, 'Q': 31, 'W': 26, ']': 18, 'c': 17,
    'i': 15, 'o': 20, 'u': 17, '{': 18, '"': 6, '(': 12, '.': 4,
    '4': 21, ':': 8, '@': 32, 'F': 20, 'L': 16, 'R': 28, 'X': 18,
    '^': 7, 'd': 25, 'j': 20, 'p': 25, 'v': 13, '|': 12, '#': 24,
    ')': 12, '/': 10, '5': 27, ';': 11, 'A': 24, 'G': 25, 'M': 28,
    'S': 25, 'Y': 14, '_': 8, 'e': 23, 'k': 21, 'q': 25, 'w': 19,
    '}': 18, '$': 29, '*': 17, '0': 22, '6': 26, '<': 10, 'B': 29,
    'H': 25, 'N': 25, 'T': 16, 'Z': 22, '`': 3, 'f': 18, 'l': 16,
    'r': 13, 'x': 13, '~': 9, '%': 22, '+': 13, '1': 19, '7': 16,
    '=': 14, 'C': 20, 'I': 18, 'O': 26, 'U': 23, '[': 18, 'a': 23,
    'g': 30, 'm': 22, 's': 21, 'y': 24,
}


def get_char_cost(ch: str) -> int:
    """Return printing cost for specific char"""
    default_cost = 23
    return ascii_costs[ch] if ch in ascii_costs else default_cost


def PrintingCosts(input_string: str) -> int:
    """Return total printing cost for given string"""
    print_cost_list = [get_char_cost(ch) for ch in input_string]
    return sum(print_cost_list)
