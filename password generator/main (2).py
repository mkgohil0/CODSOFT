import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Choose easy, medium, or strong.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return

        complexity = input("Choose complexity level (easy / medium / strong): ").lower()
        password = generate_password(length, complexity)

        if password:
            print(f"Generated Password ({complexity}): {password}")
    except ValueError:
        print("Invalid input. Please enter a number for length.")

if __name__ == "__main__":
    main()