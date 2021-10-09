# pet class
class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print(f"{self.name} is sleeping!")

    def eat(self):
        print(f"{self.name} is eating!")
    
    def play(self):
        print(f"{self.name} is playing!")
    
    def noise(self):
        print(f"{self.name} is making noise!")