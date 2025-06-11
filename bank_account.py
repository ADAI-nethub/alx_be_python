class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance"""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Remove money if sufficient funds exist"""
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Show current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")

# Example usage:
account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
account.display_balance()

