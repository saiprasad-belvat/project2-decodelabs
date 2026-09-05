"""
test_caesar_cipher.py

Automated tests for Project 2 - Basic Encryption & Decryption (Caesar Cipher).

Run with (from the project2-caesar-cipher/ folder):
    python -m unittest tests/test_caesar_cipher.py -v

or simply:
    python tests/test_caesar_cipher.py
"""

import os
import sys
import unittest

# Allow running this file directly by adding the project root to the path,
# so `import caesar_cipher` works whether run as a module or as a script.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from caesar_cipher import encrypt, decrypt, validate_shift


class TestCaesarCipher(unittest.TestCase):

    # 1. Uppercase letters
    def test_uppercase_basic(self):
        self.assertEqual(encrypt("ABC", 3), "DEF")

    # 2. Wrap-around (uppercase)
    def test_uppercase_wraparound(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    # 3. Lowercase letters
    def test_lowercase_basic(self):
        self.assertEqual(encrypt("abc", 3), "def")

    # 4. Wrap-around (lowercase)
    def test_lowercase_wraparound(self):
        self.assertEqual(encrypt("xyz", 3), "abc")

    # 5. Spaces
    def test_spaces_preserved(self):
        self.assertEqual(encrypt("HELLO WORLD", 3), "KHOOR ZRUOG")

    # 6. Punctuation
    def test_punctuation_preserved(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")

    # 7. Numbers
    def test_numbers_unchanged(self):
        self.assertEqual(encrypt("Test123", 3), "Whvw123")

    # 8. Zero shift
    def test_zero_shift(self):
        self.assertEqual(encrypt("Hello", 0), "Hello")

    # 9. Shift of exactly 26 behaves like shift 0
    def test_shift_26_behaves_like_zero(self):
        self.assertEqual(encrypt("Hello", 26), "Hello")

    # 10. Large shift normalizes correctly (29 behaves like 3)
    def test_large_shift_normalizes(self):
        self.assertEqual(encrypt("Hello", 29), encrypt("Hello", 3))

    # 11. Decryption reverses encryption exactly
    def test_decryption_reverses_encryption(self):
        original = "Hello, World!"
        shift = 3
        cipher = encrypt(original, shift)
        self.assertEqual(decrypt(cipher, shift), original)

    # 12. Round-trip validation across many inputs and shifts
    def test_round_trip_various_inputs(self):
        samples = [
            "Hello, Cyber Security!",
            "The quick brown fox jumps over the lazy dog.",
            "1234567890",
            "",
            "MiXeD CaSe with Punctuation!? #Test",
            "Newline\nand\ttab characters",
        ]
        for text in samples:
            for shift in [0, 1, 3, 13, 25, 26, 29, 52, -3, -29]:
                with self.subTest(text=text, shift=shift):
                    cipher = encrypt(text, shift)
                    self.assertEqual(decrypt(cipher, shift), text)

    # Negative shift key handling
    def test_negative_shift(self):
        # Shifting by -3 should be the same as shifting by 23
        self.assertEqual(encrypt("D", -3), encrypt("D", 23))

    # Case is preserved independently for each character
    def test_case_preservation(self):
        self.assertEqual(encrypt("AbC", 1), "BcD")

    # validate_shift: valid integer strings
    def test_validate_shift_accepts_numeric_string(self):
        self.assertEqual(validate_shift("3"), 3)
        self.assertEqual(validate_shift("29"), 3)
        self.assertEqual(validate_shift("-3"), 23)

    # validate_shift: rejects non-numeric input
    def test_validate_shift_rejects_invalid_string(self):
        with self.assertRaises(ValueError):
            validate_shift("abc")

    def test_validate_shift_rejects_none(self):
        with self.assertRaises(ValueError):
            validate_shift(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
