class BankAccount:

    def __init__(self, int_rate, balance): 
        self.interest_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", f'{self.account_balance:.2f}') # I added this float formatting to force 2 decimal places.
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.interest_rate)
        return self


aAccount = BankAccount(.05, 5000)
bAccount = BankAccount(.03, 3000)


aAccount.deposit(30).deposit(500).deposit(90).yield_interest().display_account_info()

bAccount.deposit(30).deposit(500).withdraw(90).withdraw(40).withdraw(90).withdraw(40).yield_interest().display_account_info()

