# Password Strength Checker 🔐

A beginner-friendly Python project that checks password strength based on length and different character types.

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Gives a strength rating:
  - Weak
  - Medium
  - Strong
- Provides simple feedback to improve password strength

## Technologies Used

- Python 3
- `getpass`
- `string`

## How to Run

Make sure Python 3 is installed on your computer.

Run the following command in the terminal:

```bash
python main.py
```

Then enter a test password when prompted.

## Password Checks

The program checks whether the password contains:

| Check | Requirement |
|---|---|
| Length | At least 8 characters |
| Uppercase | A-Z |
| Lowercase | a-z |
| Number | 0-9 |
| Special Character | !, @, #, $, etc. |

## Example

```text
--- Password Security Report ---

PASS: At least 8 characters
PASS: Uppercase letter (A-Z)
PASS: Lowercase letter (a-z)
PASS: Number (0-9)
PASS: Special character

Password Strength: Strong
```

## Note

This is a basic educational password checker. Its rating does not guarantee that a password is completely secure.

## Author

Ragu
