"""
caesar_cipher.py

Core logic for Project 2 - Basic Encryption & Decryption (Caesar Cipher).

This module implements:
    - encrypt(text, shift)
    - decrypt(text, shift)
    - validate_shift(shift)
    - encrypt_char_verbose(char, shift)   (optional debug helper)

Concept:
    Encryption : E_n(x) = (x + n) mod 26
    Decryption : D_n(x) = (x - n) mod 26

Where:
    x = alphabet position of the character (0-25)
    n = shift / key

ASCII reference used in this project:
    Uppercase: 'A' = 65 ... 'Z' = 90
    Lowercase: 'a' = 97 ... 'z' = 122

Only alphabetic characters (A-Z, a-z) are transformed. Everything else
(spaces, punctuation, digits, newlines, symbols) is passed through unchanged.

This is an EDUCATIONAL implementation. Caesar cipher is NOT secure for
protecting real sensitive data (see README.md for details).
"""

UPPER_BASE = 65   # ord('A')
LOWER_BASE = 97   # ord('a')
ALPHABET_SIZE = 26


def validate_shift(shift):
    """
    Validate and normalize a shift/key value.

    Accepts an int or a string that represents an int.
    Normalizes any shift (including negative or > 26) into the
    range 0-25 using modulo 26, since shifting by 26 is the same
    as shifting by 0, and shifting by 29 is the same as shifting by 3.

    Raises:
        ValueError: if the shift cannot be interpreted as an integer.

    Returns:
        int: normalized shift value in range [0, 25].
    """
    try:
        shift_int = int(shift)
    except (TypeError, ValueError):
        raise ValueError("Shift key must be a whole number (e.g. 3, -5, 29).")

    # Normalize into 0-25 range. Python's % already returns a
    # non-negative result for a positive modulus, even with
    # negative shift_int, e.g. (-3) % 26 == 23.
    return shift_int % ALPHABET_SIZE


def _shift_char(char, shift):
    """
    Shift a single alphabetic character by `shift` positions,
    wrapping around within its own case (upper or lower).

    Non-alphabetic characters are returned unchanged.
    """
    if char.isalpha():
        if char.isupper():
            base = UPPER_BASE
        else:
            base = LOWER_BASE

        # Step 1: ord(char)              -> ASCII value
        # Step 2: - base                 -> alphabet index (0-25)
        # Step 3: + shift                -> apply Caesar shift
        # Step 4: % 26                   -> wrap around the alphabet
        # Step 5: + base                 -> back to ASCII value
        # Step 6: chr(...)               -> back to a character
        index = (ord(char) - base + shift) % ALPHABET_SIZE
        return chr(index + base)

    # Spaces, punctuation, digits, newlines, symbols: unchanged.
    return char


def encrypt(text, shift):
    """
    Encrypt `text` using a Caesar cipher with the given shift.

    E_n(x) = (x + n) % 26

    Non-alphabetic characters (spaces, punctuation, digits, etc.)
    are left unchanged. Case is preserved.

    Args:
        text (str): the plaintext to encrypt.
        shift (int): the shift/key (any integer; normalized internally).

    Returns:
        str: the resulting ciphertext.
    """
    shift = validate_shift(shift)
    return "".join(_shift_char(char, shift) for char in text)


def decrypt(text, shift):
    """
    Decrypt `text` that was encrypted with the given shift.

    D_n(x) = (x - n) % 26

    This is implemented simply by encrypting with the negative
    (reverse) shift, which is mathematically equivalent.

    Args:
        text (str): the ciphertext to decrypt.
        shift (int): the same shift/key used to encrypt.

    Returns:
        str: the recovered plaintext.
    """
    shift = validate_shift(shift)
    reverse_shift = (-shift) % ALPHABET_SIZE
    return "".join(_shift_char(char, reverse_shift) for char in text)


def encrypt_char_verbose(char, shift):
    """
    Optional debug/verbose helper.

    Shows every intermediate step of the encryption math for a
    single character, matching the algorithm visualization in the
    project material. Returns a dictionary of the steps, or None
    if the character is not alphabetic.

    Example:
        encrypt_char_verbose('A', 3) ->
        {
            'char': 'A',
            'ascii_value': 65,
            'alphabet_index': 0,
            'shift': 3,
            'after_shift': 3,
            'after_modulo': 3,
            'final_ascii': 68,
            'encrypted_char': 'D'
        }
    """
    if not char.isalpha():
        return None

    shift = validate_shift(shift)
    base = UPPER_BASE if char.isupper() else LOWER_BASE

    ascii_value = ord(char)
    alphabet_index = ascii_value - base
    after_shift = alphabet_index + shift
    after_modulo = after_shift % ALPHABET_SIZE
    final_ascii = after_modulo + base
    encrypted_char = chr(final_ascii)

    return {
        "char": char,
        "ascii_value": ascii_value,
        "alphabet_index": alphabet_index,
        "shift": shift,
        "after_shift": after_shift,
        "after_modulo": after_modulo,
        "final_ascii": final_ascii,
        "encrypted_char": encrypted_char,
    }
