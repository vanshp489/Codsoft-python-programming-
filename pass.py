import random
import string

def generate_password(length):
    if length < 1:
        print("Password length must be at least 1.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the desired length of your password: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")