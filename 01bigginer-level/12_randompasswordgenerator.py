import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Ensure password has at least one lowercase, uppercase, digit, and symbol
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    if length > 4:
        password += random.choices(all_chars, k=length-4)

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter password length (minimum 4): "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    pwd = generate_password(length)
    if pwd:
        print(f"Generated password: {pwd}")

if __name__ == "__main__":
    main()
