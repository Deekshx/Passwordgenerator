import argparse
import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be included.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a strong password.")
    parser.add_argument("length", type=int, help="The desired length of the password.")
    parser.add_argument("--lowercase", action="store_true", help="Include lowercase letters.")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters.")
    parser.add_argument("--digits", action="store_true", help="Include digits.")
    parser.add_argument("--special-chars", action="store_true", help="Include special characters.")
    args = parser.parse_args()

    password = generate_password(args.length, args.lowercase, args.uppercase, args.digits, args.special_chars)
    print(password)
