# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        # This line will only print "Deposited: $XX.XX" - no other text before it.
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            # This line will only print "Withdrew: $XX.XX" for successful withdrawal.
            print(f"Withdrew: ${amount:.2f}")
        else:
            # This line will only print "Insufficient funds. Current Balance: $XX.XX" for insufficient funds.
            print(f"Insufficient funds. Current Balance: ${self.balance:.2f}")

    def display_balance(self):
        # This line will only print "Current Balance: $XX.XX".
        print(f"Current Balance: ${self.balance:.2f}")

        