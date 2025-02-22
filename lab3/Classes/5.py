# Create a bank account class that has attributes `owner`, `balance` and two methods `deposit` and `withdraw`.
#  Withdrawals may not exceed the available balance.
#  Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# ```python
# class Account:
#     pass
# ```

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance -=amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds for this withdrawal.")

account = Account("John", 1000)

account.deposit(500)
account.deposit(200)

account.withdraw(300)
account.withdraw(1500)