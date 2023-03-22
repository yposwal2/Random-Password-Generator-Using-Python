import random
import string

def generate_password(length):
    """Function to generate a random password of a given length"""
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the set
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password

# Example usage: generate a random password of length 10
password = generate_password(10)
print("\nRandom Password:", password)
print("\n") 

