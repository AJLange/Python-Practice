from pet import Pet

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet 

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

    def walk(self):
        print(f"Walking {self.pet}!")
        self.pet = Pet.play(self.pet)
        return self
    def feed(self):
        print(f"Feeding {self.pet} {self.pet_food}!")
        self.pet = Pet.eat(self.pet)
        return self
    def bathe(self):
        print(f"Bathing {self.pet}!")
        self.pet = Pet.noise(self.pet)
        return self
    

my_pet = Pet("Doggo", "shake", 100, 50)
my_ninja = Ninja("Satsuki", "Shinobi", "biscuits", "beef", my_pet)
my_ninja.feed().walk().bathe()

