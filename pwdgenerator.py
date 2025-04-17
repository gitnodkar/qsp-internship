import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(length))