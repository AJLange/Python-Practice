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

calli = User("Mori Calliope", "calli@python.com")
gura = User("Gawr Gura", "gura@python.com")
amelia = User("Amelia Watson", "ame@python.com")

calli.make_deposit(1000000)
calli.make_deposit(170000)
calli.make_withdrawl(40) #kazoo money
calli.make_withdrawl(10) #wine money

calli.display_user_balance()

gura.make_deposit(2000000)
gura.make_withdrawl(30) #pizza money
gura.make_withdrawl(2000) #bathtub money
gura.make_withdrawl(4000) #big Atlantis party

gura.display_user_balance()

calli.transfer_money(amelia, 42069) #time travel fees

calli.display_user_balance()
amelia.display_user_balance()
