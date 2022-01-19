class Pet:
    def __init__(self, type, tricks, health, energy ):
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
    def __repr__(self):
        return f"{self.type}"
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("Woof!")
        return self
    
