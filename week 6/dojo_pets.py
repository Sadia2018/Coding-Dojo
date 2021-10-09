# ninja class
class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet('raphael\'s pet', 'german_shepherd','jumps_flips','very healthy','100%')
        self.treats = treats
        self.pet_food = pet_food
    

    def walk(self):
        print(f"{self.first_name} walks!")
    
    def feed(self):
        print(f"{self.first_name} is feeding !")

    def bathe(self):
        print(f"{self.first_name} is bathing")

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

#child class cats
class cats(Pet):
    pass


#instances 
first_ninja = Ninja('raphael','khan','cesar','dog bites','the_best_food')
german_shepherd = Pet('raphael\'s pet', 'german_shepherd','jumps_flips','very healthy','100%')

print(first_ninja.pet.type)