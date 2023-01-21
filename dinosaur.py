
class Dinosaur:
    def __init__(self, name, ap):
        self.name = name
        self.health = 100
        self.attack_power = ap

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name} for {self.attack_power}! {robot.name} is left with {robot.health} health.")

    
