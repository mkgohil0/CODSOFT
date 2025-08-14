import random
import string

def generate_password():
    """
    Generates a strong, random password based on user-specified length.
    """
    print("--- Password Generator ---")
    
    # --- 1. User Input ---
    # Prompt the user for the desired password length and validate the input.
    try:
        length = int(input("Enter the desired length for the password (minimum 8): "))
        if length < 8:
            print("For a strong password, the length should be at least 8. Setting length to 8.")
            length = 8
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    # --- 2. Generate Password ---
    # Define the character sets to use for the password.
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets into a single pool.
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate a password by randomly choosing characters from the pool.
    # The ''.join() method concatenates the list of characters into a final string.
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # --- 3. Display the Password ---
    print("\n" + "="*25)
    print(f"Generated Password: {password}")
    print("="*25 + "\n")


# Run the password generator function
generate_password()