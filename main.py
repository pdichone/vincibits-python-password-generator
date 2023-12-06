import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Ensure the password is always strong by including at least one of each character type
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)

    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    return "".join(password)


def main():
    try:
        length = int(
            input("Enter the desired length of the password (minimum 4 characters): ")
        )
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
