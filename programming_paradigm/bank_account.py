# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        # Change from :.2f to :.1f to get $XX.0 instead of $XX.00
        print(f"Deposited: ${amount:.1f}") # <--- UPDATED LINE

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")
        else:
            print(f"Insufficient funds. Current Balance: ${self.balance:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.1f}")