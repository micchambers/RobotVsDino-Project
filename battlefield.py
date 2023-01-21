from dinosaur import Dinosaur 

from robot import Robot

class Battleground:

    def __init__(self, name):
        self.name = name
        self.dinosaur = Dinosaur("Hydrasaurus", 20)
        self.robot = Robot("Poebot")

    def run_game(self):
        self.display_welcome()
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)

    def display_welcome(self):
        print("Welcome to the " + self.name)

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
 
