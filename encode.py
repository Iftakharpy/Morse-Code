from code_map import MORSE_CODES, REVERSE_MORSE_CODES
from checkers import is_valid_morse, is_encodable


INVALID_MESSAGE = "isn't present in code_map.py can't encode the message."


def encode_message(message):
    encode_able = is_encodable(message)
    if encode_able!=True:
        print(f"`{encode_able}` {INVALID_MESSAGE}\n")
        return

    encoded = []
    for char in message:
        encoded.append(MORSE_CODES[char.upper()])
    return " ".join(encoded)


def decode_message(message):
    if not message:
        return
    if not is_valid_morse(message):
        print(f"`{message}` contains invalid morse code characters."+
                "\nValid morse code characters are (space, dot, hyphen/minus)[ .-]")
        return
    decoded = []
    
    space_len = len(MORSE_CODES[" "])
    spaces = 0
    decoded_len = 0

    char = ""
    while decoded_len<len(message):
        curr_char = message[decoded_len]
        if curr_char == " ":
            try:
                decoded.append(REVERSE_MORSE_CODES[char])
            except KeyError:
                pass
            char = ""
            spaces+=1
            if spaces%space_len == 0:
                decoded.append(" ")
            decoded_len+=1
            continue
        else:
            spaces = 0
            char += curr_char
        decoded_len+=1
    return "".join(decoded)
