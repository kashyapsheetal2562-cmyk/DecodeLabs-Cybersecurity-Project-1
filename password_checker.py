import re
import getpass


# Common passwords that should not be considered strong
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "abc123",
    "iloveyou"
}


def check_password_strength(password):
    """Analyze password security and return strength, score and feedback."""

    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Extra point for longer passwords
    if len(password) >= 12:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        return "WEAK", 0, [
            "This password is commonly used and unsafe."
        ]

    # Strength classification
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, feedback


def display_result(password):
    """Display password analysis without displaying the password itself."""

    strength, score, feedback = check_password_strength(password)

    uppercase = bool(re.search(r"[A-Z]", password))
    lowercase = bool(re.search(r"[a-z]", password))
    number = bool(re.search(r"\d", password))
    special = bool(re.search(r"[^A-Za-z0-9]", password))
    minimum_length = len(password) >= 8

    print("\n" + "=" * 45)
    print("       PASSWORD SECURITY ANALYSIS")
    print("=" * 45)

    print(f"Password Length : {len(password)} characters")
    print(f"Security Score  : {score}/6")
    print(f"Strength        : {strength}")

    print("\nSecurity Checks:")

    print(f"  Uppercase      : {'PASS' if uppercase else 'FAIL'}")
    print(f"  Lowercase      : {'PASS' if lowercase else 'FAIL'}")
    print(f"  Number         : {'PASS' if number else 'FAIL'}")
    print(f"  Special Symbol : {'PASS' if special else 'FAIL'}")
    print(f"  Minimum Length : {'PASS' if minimum_length else 'FAIL'}")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"  - {item}")
    else:
        print("\nAll basic security requirements are satisfied.")

    print("=" * 45)


def main():
    print("=" * 45)
    print("     DecodeLabs Password Strength Checker")
    print("=" * 45)

    print("\nEnter a password to evaluate its strength.")
    print("Your password will not be displayed on screen.")

    password = getpass.getpass("\nPassword: ")

    if not password:
        print("\nError: Password cannot be empty.")
        return

    display_result(password)


if __name__ == "__main__":
    main()
