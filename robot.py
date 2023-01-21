from weapon import Weapon

from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Sword", 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} for {self.active_weapon.attack_power}! {dinosaur.name} is left with {dinosaur.health} health.")
        
        
        
     






    