class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # ✅ Fixed: subtract from balance
            print(f"Withdrew: ${amount:.1f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
if __name__ == "__main__":
    acc = BankAccount(100)
    acc.deposit(67)
    acc.withdraw(50)
    acc.withdraw(150)
    acc.display_balance()
