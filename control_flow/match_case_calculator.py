# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match-case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()  # Exit the program if division by zero
        result = num1 / num2
    case _:  # Default case for invalid operations
        print("Invalid operation selected.")
        exit()

print(f"The result is {result}")
