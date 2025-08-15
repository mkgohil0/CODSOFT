# calculator.py

def calculator():
    """
    A simple calculator that performs basic arithmetic operations
    based on user input.
    """
    print("Welcome to the simple calculator!")
    
    # --- Get the first number from the user ---
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break  # Exit the loop if the input is a valid number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # --- Get the operation from the user ---
    while True:
        operator = input("Enter an operation (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            break  # Exit the loop if the operator is valid
        else:
            print("Invalid operation. Please enter one of +, -, *, /")

    # --- Get the second number from the user ---
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break  # Exit the loop if the input is a valid number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # --- Perform the calculation and display the result ---
    if operator == '+':
        result = num1 + num2
        print(f"The result is: {num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"The result is: {num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"The result is: {num1} * {num2} = {result}")
    elif operator == '/':
        # Handle the division by zero error
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is: {num1} / {num2} = {result}")

# --- Run the calculator function ---
if __name__ == "__main__":
    calculator()