# programming_paradigm/bank_account.py - Optimized for main-0.py interaction

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance # Use 'balance' consistently

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # Use 'balance' consistently
            return True  # Indicate success, main-0.py will print "Deposited: $X.X"
        else:
            return False # Indicate failure (e.g., non-positive amount)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance: # Added check for positive amount
            self.balance -= amount
            return True  # Indicate success, main-0.py will print "Withdrew: $X.X"
        else:
            return False # Indicate failure (insufficient funds or non-positive amount), main-0.py will print "Insufficient funds."

    def display_balance(self):
        # This method will still print directly, but use the correct attribute and formatting
        print(f"Current Balance: ${self.balance:.1f}") # Use 'balance' and :.1f for consistency