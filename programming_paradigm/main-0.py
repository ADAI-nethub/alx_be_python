# main-0.py (Optimized for compatibility and ALX print formats)

import sys
from bank_account import BankAccount # Ensure this correctly imports your BankAccount class

def main():
    # Create an account with $100 starting balance
    account = BankAccount(100) # This uses the __init__ with initial_balance=0

    # Check for proper command line usage
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>") # Corrected script name
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount
    # Handle cases where amount might not be provided for 'display'
    parts = sys.argv[1].split(':', 1) # Split only on the first colon
    command = parts[0]
    amount_str = parts[1] if len(parts) > 1 else None

    amount = None
    if amount_str is not None:
        try:
            amount = float(amount_str)
        except ValueError:
            print("Error: Amount must be a number.")
            sys.exit(1)

    # Execute the appropriate command and handle printing
    if command == "deposit":
        if amount is None or amount <= 0: # Ensure amount is valid for deposit
            print("Deposit amount must be positive.")
        else:
            # BankAccount.deposit now returns True/False
            if account.deposit(amount):
                print(f"Deposited: ${amount:.1f}") # Print success message here
            # No 'else' needed here for deposit, as main-0.py handles the error condition
    elif command == "withdraw":
        if amount is None or amount <= 0: # Ensure amount is valid for withdraw
            print("Withdrawal amount must be positive.")
        else:
            # BankAccount.withdraw now returns True/False
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.1f}") # Print success message here
            else:
                print("Insufficient funds.") # Print insufficient funds message here
    elif command == "display":
        # BankAccount.display_balance prints directly, so just call it
        account.display_balance()
    else:
        print("Invalid command.") # This covers unrecognized commands
        sys.exit(1)

if __name__ == "__main__":
    main()