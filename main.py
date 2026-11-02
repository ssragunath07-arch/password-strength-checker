import string


def check_password_strength(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter (A-Z)": any(c.isupper() for c in password),
        "Lowercase letter (a-z)": any(c.islower() for c in password),
        "Number (0-9)": any(c.isdigit() for c in password),
        "Special character": any(
            c in string.punctuation for c in password
        ),
    }

    score = sum(checks.values())

    if len(password) < 8:
        strength = "Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return checks, strength


def main():
    print("=" * 40)
    print("     PASSWORD STRENGTH CHECKER")
    print("=" * 40)
    print("This is an educational password checker.")
    print()

    password = input("Enter a test password: ")

    checks, strength = check_password_strength(password)

    print("\n--- Password Security Report ---")
    print()

    for rule, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {rule}")

    print(f"\nPassword Strength: {strength}")

    if strength == "Weak":
        print("Tip: Use a longer, unique password.")
    elif strength == "Medium":
        print("Tip: Add any missing character types.")
    else:
        print("Good! Consider using a longer passphrase.")

    print("\nNote: This is a basic educational checker.")
    print("It does not guarantee that a password is secure.")


if __name__ == "__main__":
    main()
