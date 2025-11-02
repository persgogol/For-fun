"""
Caesar Cipher Encoder/Decoder

This script allows the user to encrypt or decrypt text using the Caesar cipher.
The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet.
Non-alphabetical characters are left unchanged.

Usage:
1. Choose whether to encode or decode.
2. Input the message.
3. Input the shift value (an integer between 0 and 25).

Functions:
- caesar_encode(message, shift): Returns the encoded message.
- caesar_decode(message, shift): Returns the decoded message.

Author: Anonymous
Date: 2025-10-18
"""


def caesar_encode(message: str, shift: int) -> str:
    """Encode a message using the Caesar cipher."""
    encoded = []
    for ch in message:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            # Compute shifted position wrapping around the alphabet
            offset = (ord(ch) - start + shift) % 26
            encoded.append(chr(start + offset))
        else:
            encoded.append(ch)
    return ''.join(encoded)


def caesar_decode(message: str, shift: int) -> str:
    """Decode a message encoded with the Caesar cipher."""
    return caesar_encode(message, -shift)


def get_shift_input() -> int:
    """Prompt the user for a valid shift value between 0 and 25."""
    while True:
        try:
            shift = int(input("Enter shift value (0-25): ").strip())
            if 0 <= shift <= 25:
                return shift
            else:
                print("Shift must be between 0 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 25.")


def main():
    print("Caesar Cipher Encoder/Decoder")
    print("-----------------------------")
    print("1. Encode a message")
    print("2. Decode a message")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        message = input("Enter the message to encode: ")
        shift = get_shift_input()
        encoded_message = caesar_encode(message, shift)
        print(f"Encoded message: {encoded_message}")
    elif choice == "2":
        message = input("Enter the message to decode: ")
        shift = get_shift_input()
        decoded_message = caesar_decode(message, shift)
        print(f"Decoded message: {decoded_message}")
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")


if __name__ == "__main__":
    main()
