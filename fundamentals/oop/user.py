# declare a class and give it name User
class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0

        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawl(self, amount):	# takes an argument that is the amount of the withdraw
        self.account_balance -= amount	# the specific user's account decreases by the amount of the value received
    
    def display_user_balance(self): #print the user's name and account balance to terminal
        print(self.name, "Balance: $", self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount #remove this balance from user's account
        other_user.account_balance += amount #add it to the other user



# various tests

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(monty.name)	# output: Monty Python


guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50


guido.make_withdrawl(50)
print(guido.account_balance)	# output: 250

guido.display_user_balance()   # output: Balance: $ 250

guido.transfer_money(monty, 50)
print(guido.account_balance)	# output: 200
print(monty.account_balance)	# output: 100
