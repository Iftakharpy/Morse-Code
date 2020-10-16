import re
from code_map import MORSE_CODES


INVALID_MC_REGEXP = re.compile(r"[^ .-]+")

def is_valid_morse(message):
    return not bool(re.search(INVALID_MC_REGEXP, message))

def is_encodable(message):
    for char in message:
        char = char.upper()
        if not char in MORSE_CODES:
            return char
    return True
