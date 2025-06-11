# programming_paradigm/bank_account.py

class BankAccount:
    """
    A simple BankAccount class to manage a balance.
    """
    def __init__(self, initial_balance=0):
        # Initialize the balance. Balance should be private (encapsulation).
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__balance = initial_balance

    def deposit(self, amount):
        # Implement deposit logic.
        # Ensure amount is positive.
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Deposit amount must be a positive number."
        self.__balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        # Implement withdraw logic.
        # Ensure amount is positive.
        # Check for sufficient funds.
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Withdrawal amount must be a positive number."
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        return f"Withdrew: ${amount}"

    def get_balance(self):
        # Return the current balance.
        return self.__balance