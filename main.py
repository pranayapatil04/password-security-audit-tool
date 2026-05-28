import re
import bcrypt
import random
import string

# Common password list
common_passwords = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "admin",
    "welcome"
]

# Function to check password strength
def check_password_strength(password):

    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Number
    if re.search(r"[0-9]", password):
        score += 1

    # Special character
    if re.search(r"[@$!%*?&]", password):
        score += 1

    return score

# Function to estimate crack time
def estimate_crack_time(password):

    combinations = 0

    if re.search(r"[a-z]", password):
        combinations += 26

    if re.search(r"[A-Z]", password):
        combinations += 26

    if re.search(r"[0-9]", password):
        combinations += 10

    if re.search(r"[@$!%*?&]", password):
        combinations += 10

    possible_passwords = combinations ** len(password)

    guesses_per_second = 1000000000

    seconds = possible_passwords / guesses_per_second

    return seconds

# Function to suggest stronger password
def generate_strong_password():

    characters = string.ascii_letters + string.digits + "@$!%*?&"

    strong_password = ''.join(random.choice(characters) for i in range(12))

    return strong_password

# Function to hash password
def hash_password(password):

    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed

# Main Program
password = input("Enter your password: ")

# Check common password
if password in common_passwords:
    print("\nWARNING: This is a very common password!")

# Strength Check
strength = check_password_strength(password)

print("\nPassword Strength Score:", strength, "/5")

if strength <= 2:
    print("Weak Password")
elif strength == 3 or strength == 4:
    print("Moderate Password")
else:
    print("Strong Password")

# Crack Time
seconds = estimate_crack_time(password)

print(f"\nEstimated crack time: {seconds:.2f} seconds")

# Suggest stronger password
print("\nSuggested Strong Password:")
print(generate_strong_password())

# Hash password
hashed_password = hash_password(password)

print("\nSecure Hashed Password:")
print(hashed_password.decode())