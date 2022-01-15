#associating accounts with users, though they are in the same file here for now

class BankAccount:

    def __init__(self, int_rate, balance): 
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", f'{self.balance:.2f}') # I added this float formatting to force 2 decimal places.
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self


class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account is an instance of BankAccount
        self.account = BankAccount(int_rate=0.02, balance=0)

        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawl(self, amount):	# takes an argument that is the amount of the withdraw
        self.account.balance -= amount	# the specific user's account decreases by the amount of the value received
    
    def display_user_balance(self): #print the user's name and account balance to terminal
        print(self.name, "Balance: $", self.account.balance)
    
    ''' 
    this one doesn't work anymore for now 
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount #remove this balance from user's account
        other_user.account.balance += amount #add it to the other user
    '''


# various tests go here
sana = User("Tsukumo Sana", "sanaisbig@python.com")
sana.make_deposit(3000)
sana.display_user_balance()
sana.make_withdrawl(400)
sana.display_user_balance()

# didn't do bonus, will do later maybe
