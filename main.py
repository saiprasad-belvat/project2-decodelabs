"""
main.py

DecodeLabs Cyber Security Industrial Training Kit - Batch 2026
Project 2 - Basic Encryption & Decryption (Caesar Cipher)

Application flow (IPO Model):

    INPUT   -> plaintext + shift key from the user
    PROCESS -> Caesar cipher encryption, then decryption with the same key
    OUTPUT  -> ciphertext, recovered plaintext, and a validation result

Run with:
    python main.py
"""

from caesar_cipher import encrypt, decrypt, validate_shift, encrypt_char_verbose


BANNER = r"""
==============================================
       DECodeLabs - Project 2
    BASIC ENCRYPTION & DECRYPTION
            Caesar Cipher
==============================================
"""

SECURITY_NOTE = """
[i] Security note:
    Caesar cipher is an EDUCATIONAL cipher only.
    - Tiny key space: only 25 meaningful shifts exist, so an attacker
      can brute-force every shift almost instantly.
    - Pattern preservation: letter frequencies are unchanged, so
      frequency analysis can reveal the shift quickly.
    Do not use this to protect real, sensitive information.
    Modern systems use algorithms such as AES instead.
"""


def get_plaintext():
    """Prompt the user for plaintext. Handles empty input gracefully."""
    text = input("Enter plaintext:\n> ")
    if text == "":
        print("[!] You entered empty text. Encrypting an empty string is fine,")
        print("    but there will be nothing to show. Continuing anyway.\n")
    return text


def get_shift():
    """
    Prompt the user for a shift/key, validating it as an integer.
    Re-prompts on invalid input instead of crashing.
    Large or negative shifts are normalized (handled inside validate_shift).
    """
    while True:
        raw = input("Enter shift key:\n> ")
        try:
            shift = validate_shift(raw)
            return shift
        except ValueError as e:
            print(f"[!] Invalid shift key: {e} Please try again.\n")


def maybe_show_verbose(plaintext, shift):
    """
    Optional verbose/debug mode: shows the algorithm's intermediate
    math for the first alphabetic character in the plaintext.
    """
    choice = input("\nShow step-by-step math for the first letter? (y/n): ").strip().lower()
    if choice != "y":
        return

    for char in plaintext:
        details = encrypt_char_verbose(char, shift)
        if details:
            print("\n----------------------------------------")
            print("Algorithm Visualization")
            print("----------------------------------------")
            print(f"Character:        {details['char']}")
            print(f"ASCII value:      {details['ascii_value']}")
            print(f"Alphabet index:   {details['alphabet_index']}")
            print(f"Shift:            {details['shift']}")
            print(f"After shift:      {details['after_shift']}")
            print(f"After modulo 26:  {details['after_modulo']}")
            print(f"Final ASCII:      {details['final_ascii']}")
            print(f"Encrypted char:   {details['encrypted_char']}")
            return
    print("[i] No alphabetic characters found to visualize.")


def main():
    print(BANNER)

    # ---- INPUT ----
    plaintext = get_plaintext()
    shift = get_shift()

    maybe_show_verbose(plaintext, shift)

    # ---- PROCESS: ENCRYPTION ----
    print("\n[+] Encrypting...")
    ciphertext = encrypt(plaintext, shift)

    print("\n----------------------------------------")
    print("Plaintext:")
    print(plaintext)
    print("\nShift:")
    print(shift)
    print("\nCiphertext:")
    print(ciphertext)

    # ---- PROCESS: DECRYPTION ----
    print("\n[+] Decrypting...")
    decrypted_text = decrypt(ciphertext, shift)

    print("\n----------------------------------------")
    print("Decrypted text:")
    print(decrypted_text)

    # ---- VALIDATION ----
    print("\n----------------------------------------")
    if decrypted_text == plaintext:
        print("[\u2713] Validation successful!")
        print("Decrypted text matches original plaintext.")
    else:
        # This branch should never trigger if the logic is correct;
        # it exists to make the validation step explicit and visible.
        print("[x] Validation FAILED!")
        print("Decrypted text does NOT match original plaintext.")

    print(SECURITY_NOTE)
    print("==============================================")


if __name__ == "__main__":
    main()
