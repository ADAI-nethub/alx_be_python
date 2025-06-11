# programming_paradigm/main-0.py

import sys
from bank_account import BankAccount # Import the class from the other file

# Initialize a bank account. For a simple command-line tool,
# the balance might reset each time, or you could store it (more advanced).
# For this task, assume a starting balance for demonstration.
# Let's start with a fixed initial balance, e.g., $100 for testing.
account = BankAccount(100) # Initial balance for testing

def run_cli_command():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<value>]")
        return

    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    value_str = command_parts[1] if len(command_parts) > 1 else None

    if command == 'deposit':
        try:
            amount = float(value_str)
            print(account.deposit(amount))
        except (ValueError, TypeError):
            print("Invalid deposit amount.")
    elif command == 'withdraw':
        try:
            amount = float(value_str)
            print(account.withdraw(amount))
        except (ValueError, TypeError):
            print("Invalid withdrawal amount.")
    elif command == 'display':
        print(f"Current Balance: ${account.get_balance()}")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    run_cli_command()