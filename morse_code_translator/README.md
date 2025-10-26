MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-'
}


def encode(message):
    """
    Encode a string into Morse code.

    Args:
        message (str): The message to encode.

    Returns:
        str: Encoded Morse code where letters are separated by spaces.
    """
    return ' '.join(MORSE_CODE_DICT.get(ch.upper(), '') for ch in message)


def decode(morse_code):
    """
    Decode a Morse code string into plain text.

    Args:
        morse_code (str): Morse code with symbols separated by spaces.

    Returns:
        str: Decoded plain text.
    """
    inverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(inverse_dict.get(code, '') for code in morse_code.split())


if __name__ == "__main__":
    sample = "Hello World 123"
    encoded = encode(sample)
    print("Encoded:", encoded)
    decoded = decode(encoded)
    print("Decoded:", decoded)
