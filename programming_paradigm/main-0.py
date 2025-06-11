# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Create an account with $100 starting balance
    account = BankAccount(100)
    
    # Check for proper command line usage
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute the appropriate command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()