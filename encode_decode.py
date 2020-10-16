from code_map import MORSE_CODES, REVERSE_MORSE_CODES
from checkers import is_valid_morse, is_encodable

VALID_MORSE_CODE_CHARS = [" ", ".", "-"]
INVALID_MESSAGE_ENCODE = "isn't present in code_map.py can't encode the message."
INVALID_MESSAGE_DECODE = f"""contains invalid morse code characters.
{VALID_MORSE_CODE_CHARS} these are only valid morse code characters
"""


def encode_message(message):
    encode_able = is_encodable(message)
    if encode_able!=True:
        print(f"`{encode_able}` {INVALID_MESSAGE_ENCODE}\n")
        return

    encoded = []
    for char in message:
        encoded.append(MORSE_CODES[char.upper()])
    return " ".join(encoded)


def decode_message(message):
    if not message:
        return
    if not is_valid_morse(message):
        print(f"`{message}` {INVALID_MESSAGE_DECODE}")
        return
    decoded = []
    
    space_len = len(MORSE_CODES[" "])
    spaces = 0
    decoded_len = 0
    msg_len = len(message)

    char = ""
    while decoded_len<msg_len:
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

        decoded_len += 1

        if char and decoded_len == msg_len:
            decoded.append(REVERSE_MORSE_CODES[char])
    
    return "".join(decoded)
