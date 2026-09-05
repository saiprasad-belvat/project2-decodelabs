# Project 2 - Basic Encryption & Decryption

**DecodeLabs Cyber Security Industrial Training Kit — Batch 2026**
**Theme:** Confidentiality Logic — Basic Encryption and Decryption using a Caesar Cipher

---

## 1. Project Overview

This project implements a **Caesar cipher**, one of the oldest and simplest
encryption techniques, to demonstrate the fundamental mechanics of
encryption and decryption. The user provides a message (plaintext) and a
shift key. The program encrypts the message into ciphertext, then decrypts
it back and validates that the original message is recovered exactly.

This is an **educational** implementation. It is not intended to protect
real, sensitive data.

## 2. Objective

> "Implement a simple encryption and decryption technique."

The project teaches:

- Basic encryption and decryption concepts
- Logical, reversible transformation
- Data confidentiality
- Mathematical/programmatic data transformation using ASCII values and
  modular arithmetic
- Clean, function-based logic building

## 3. Cybersecurity Concept: Data Confidentiality

**Data confidentiality** means ensuring that information is only readable
by authorized parties. Data in motion (e.g. sent across a network) cannot
be protected by physical walls — it is exposed. The solution is
**mathematical transformation**: converting readable plaintext into
unreadable ciphertext so that anyone intercepting it cannot understand it
without the key.

```
PLAINTEXT (raw data)
      |
      v
ALGORITHM + KEY
      |
      v
CIPHERTEXT (secured data)
```

Decryption reverses this using the same algorithm and key:

```
CIPHERTEXT
      |
      v
ALGORITHM + KEY (reverse)
      |
      v
PLAINTEXT
```

- **Plaintext** — the original, readable data
- **Ciphertext** — the transformed, unreadable data
- **Key** — the shift value used by the Caesar cipher
- **Algorithm** — the transformation process (Caesar shift)

## 4. What is a Caesar Cipher?

A Caesar cipher is a **mono-alphabetic substitution cipher**: every letter
in the plaintext is replaced by a letter a fixed number of positions ("the
shift" or "key") further along in the alphabet, wrapping back to the start
after `Z`.

Example with shift 3:

```
A -> D
B -> E
C -> F
...
X -> A
Y -> B
Z -> C
```

## 5. How Encryption Works

Each alphabetic character is converted to a number (its position in the
alphabet, 0-25), shifted forward by the key, wrapped using modulo 26, and
converted back to a character.

## 6. How Decryption Works

Decryption applies the **same shift in reverse** (subtracting instead of
adding). Because Caesar cipher is symmetric, the same key that locks the
message also unlocks it.

## 7. Mathematical Formula

**Encryption:**

```
E_n(x) = (x + n) mod 26
```

**Decryption:**

```
D_n(x) = (x - n) mod 26
```

Where:

- `x` = the alphabet position of the character (0-25)
- `n` = the shift/key

## 8. ASCII Conversion

Computers store characters as numbers (ASCII values). Before any math can
be applied, characters must be converted to numbers, and afterward
converted back.

## 9. `ord()` and `chr()`

- **`ord(char)`** — converts a character into its ASCII integer.
  Example: `ord('A') == 65`
- **`chr(number)`** — converts an integer back into a character.
  Example: `chr(65) == 'A'`

ASCII ranges used in this project:

| Case      | Start | End |
|-----------|-------|-----|
| Uppercase | A = 65 | Z = 90 |
| Lowercase | a = 97 | z = 122 |

## 10. Modulo 26

The English alphabet has 26 letters, so all shift arithmetic is done
`% 26` to "wrap around" once the count runs past `Z` (or `z`).

**Worked example:** Encrypt `Y` with shift 3.

```
Y has alphabet position 24
24 + 3 = 27
27 % 26 = 1
1 corresponds to B
Therefore: Y + 3 = B
```

## 11. Handling Uppercase

```python
cipher_char = chr((ord(char) - 65 + shift) % 26 + 65)
```

Steps:

1. `ord(char)` — convert character to ASCII
2. `- 65` — convert ASCII to alphabet index (0-25)
3. `+ shift` — apply the Caesar shift
4. `% 26` — wrap within the alphabet
5. `+ 65` — convert back to uppercase ASCII
6. `chr(...)` — convert back to a character

Worked example — `A` with shift 3:

```
ord('A')      = 65
65 - 65       = 0
0 + 3         = 3
3 % 26        = 3
3 + 65        = 68
chr(68)       = 'D'
Therefore: A -> D
```

Decryption uses the mirror formula:

```python
plain_char = chr((ord(char) - 65 - shift) % 26 + 65)
```

## 12. Handling Lowercase

Lowercase letters use base `97` instead of `65`. Case is preserved — an
uppercase letter always encrypts to an uppercase letter, and lowercase to
lowercase.

```python
# Encryption
chr((ord(char) - 97 + shift) % 26 + 97)

# Decryption
chr((ord(char) - 97 - shift) % 26 + 97)
```

Examples: `a -> d`, `x -> a` (wrap-around), `z -> c` (wrap-around).

## 13. Handling Spaces and Punctuation

Only alphabetic characters (`A-Z`, `a-z`) are transformed. Everything else
— spaces, punctuation, digits, symbols, newlines — passes through
**unchanged**.

Example (shift 3):

```
Input:  Hello, World! 123
Output: Khoor, Zruog! 123
```

## 14. User-Defined Shift Key

The user supplies their own shift key at runtime. The key is:

- Validated as an integer (re-prompted if invalid, e.g. `"abc"`)
- Normalized with `% 26`, so `26` behaves like `0`, and `29` behaves like `3`
- Supported for negative values (e.g. `-3` behaves like `23`)

## 15. IPO Model

**Encryption**

| Stage | Description |
|-------|-------------|
| Input | Plaintext / raw user data |
| Process | Caesar cipher encryption algorithm + key |
| Output | Ciphertext / secured transformed data |

**Decryption**

| Stage | Description |
|-------|-------------|
| Input | Ciphertext |
| Process | Reverse Caesar cipher algorithm using the same key |
| Output | Original plaintext |

## 16. Algorithm Flow

**Encryption path:**

```
PLAINTEXT -> INPUT -> ASCII CONVERSION -> CAESAR SHIFT -> MODULO 26 -> CIPHERTEXT
```

**Decryption path:**

```
CIPHERTEXT -> REVERSE SHIFT -> MODULO 26 -> PLAINTEXT
```

**Application flow:**

```
START
  -> Display project title
  -> Ask user for plaintext
  -> Ask user for shift/key
  -> Validate input
  -> Encrypt plaintext
  -> Display ciphertext
  -> Decrypt ciphertext
  -> Display decrypted plaintext
  -> Validate decrypted_text == original_text
  -> Display validation result
END
```

## 17. Example

```
========================================
        CAESAR CIPHER
 Basic Encryption & Decryption
========================================

Enter plaintext:
Hello, World!

Enter shift key:
3

----------------------------------------
Encrypted Text:
Khoor, Zruog!

----------------------------------------
Decrypted Text:
Hello, World!

----------------------------------------
Validation:
Encryption/Decryption successful!
Original text matches decrypted text.
========================================
```

## 18. Installation

No external dependencies are required — only the Python standard library.

```bash
git clone <this-repo-url>
cd project2-caesar-cipher
```

(Optional, since there is nothing to install:)

```bash
pip install -r requirements.txt
```

Requires Python 3.6+.

## 19. Usage

Run the interactive CLI:

```bash
python main.py
```

You will be prompted for plaintext and a shift key. The program then
displays the ciphertext, the decrypted text, and a validation result. You
can also opt into a step-by-step "algorithm visualization" for the first
letter of your message.

You can also use the functions directly in your own scripts:

```python
from caesar_cipher import encrypt, decrypt

cipher = encrypt("Hello, World!", 3)   # "Khoor, Zruog!"
plain = decrypt(cipher, 3)             # "Hello, World!"
```

## 20. Testing

Automated tests live in `tests/test_caesar_cipher.py` and cover every case
in the validation checklist below.

Run them with:

```bash
python -m unittest tests/test_caesar_cipher.py -v
```

or:

```bash
python tests/test_caesar_cipher.py
```

Test cases included:

1. Uppercase letters (`ABC` + shift 3 -> `DEF`)
2. Uppercase wrap-around (`XYZ` + shift 3 -> `ABC`)
3. Lowercase letters (`abc` + shift 3 -> `def`)
4. Lowercase wrap-around (`xyz` + shift 3 -> `abc`)
5. Spaces preserved (`HELLO WORLD` + shift 3 -> `KHOOR ZRUOG`)
6. Punctuation preserved (`Hello, World!` + shift 3 -> `Khoor, Zruog!`)
7. Numbers unchanged (`Test123` + shift 3 -> `Whvw123`)
8. Zero shift (`Hello` + shift 0 -> `Hello`)
9. Shift of 26 behaves like shift 0
10. Large shift (29) behaves like shift 3
11. Decryption reverses encryption exactly
12. Round-trip validation: `decrypt(encrypt(text, shift), shift) == text`
    for many texts and shifts, including negative and very large shifts

## 21. Security Limitations

The Caesar cipher provides only **basic, educational** confidentiality.
It should **not** be used to protect real sensitive data.

## 22. Caesar Cipher Vulnerabilities

### 23. Brute Force / Tiny Key Space

There are only **25 meaningful shifts** (1-25; a shift of 0 or 26 does
nothing). An attacker can simply try every possible shift and read off
whichever result looks like real language — this takes a computer a
fraction of a second.

### 24. Frequency Analysis / Pattern Preservation

The Caesar cipher preserves the **frequency pattern** of the original
language: a letter that appears often in the plaintext (like `E` in
English) still appears equally often in the ciphertext, just renamed to a
different letter. An attacker can compare letter frequencies in the
ciphertext against known English letter frequencies to deduce the shift,
even without brute-forcing every option.

## 25. Caesar Cipher vs Modern Encryption

```
Caesar Cipher -> Modern Cryptography -> AES
```

Modern algorithms like **AES (Advanced Encryption Standard)** address the
Caesar cipher's weaknesses through:

- **Confusion** — making the relationship between key and ciphertext as
  complex as possible
- **Diffusion** — spreading the influence of each plaintext bit across
  many ciphertext bits
- **128-bit (or larger) keys** — an astronomically large key space,
  making brute force infeasible
- **XOR operations** and multiple transformation rounds instead of a
  simple, fixed substitution

The Caesar cipher remains valuable as a **foundational teaching tool** for
understanding what encryption *is*, even though it is not used to secure
real systems today.

## 26. Future Improvements

- Vigenère cipher (multi-character keyword) as an optional extension
- A simple graphical interface (GUI)
- File encryption/decryption support
- Frequency-analysis "cracking" demo tool
- Support for additional alphabets/locales

*(Note: per the project requirements, the Caesar cipher remains the core,
required implementation — it is not replaced by any of the above.)*

## 27. Project Deliverables

- [x] Implement the IPO Cycle
- [x] Apply the mathematics: `ord()`, `chr()`, `% 26`
- [x] Handle edge cases: spaces, punctuation, numbers, symbols
- [x] Validate using a decryption function (round-trip check)

## 28. Conclusion

This project demonstrates the fundamentals of encryption and decryption
using a Caesar cipher: converting characters to numbers with `ord()`,
applying a reversible mathematical shift with modulo 26, and converting
back with `chr()`. It shows how a shared key can both lock (encrypt) and
unlock (decrypt) a message, introducing the core idea of **data
confidentiality** — while also being honest about why this specific
cipher is not suitable for real-world security, motivating the move
toward modern algorithms like AES.

---

## Project Structure

```
project2-caesar-cipher/
│
├── README.md
├── requirements.txt
├── main.py
├── caesar_cipher.py
│
├── tests/
│   └── test_caesar_cipher.py
│
└── screenshots/
    └── .gitkeep
```

## Final Project Checklist (mapped to DecodeLabs requirements)

- [x] User can enter plaintext
- [x] User can enter a shift key
- [x] Encryption works
- [x] Decryption works
- [x] Uppercase letters work
- [x] Lowercase letters work
- [x] Alphabet wrap-around works
- [x] Spaces remain unchanged
- [x] Punctuation remains unchanged
- [x] Numbers remain unchanged
- [x] `ord()` is used
- [x] `chr()` is used
- [x] `% 26` is used
- [x] Encryption follows `E_n(x) = (x+n) % 26`
- [x] Decryption follows `D_n(x) = (x-n) % 26`
- [x] Same key can encrypt/decrypt
- [x] Decrypted output matches original input
- [x] Invalid shift input is handled
- [x] Large shifts are handled
- [x] Tests are included
- [x] README is included
- [x] Security limitations are documented
- [x] Caesar cipher's weak security is explained
- [x] IPO model is documented
- [x] Project deliverables are satisfied
