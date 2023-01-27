from dinosaur import Dinosaur 

from robot import Robot

class Battleground:

    def __init__(self, name):
        self.name = name
        self.dinosaur = Dinosaur("Dino", 20)
        self.robot = Robot("Robo")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
 
    def display_welcome(self):
        print("Welcome to the " + self.name)

    def battle_phase(self):
        self.winner = "Undetermined"
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
                self.display_winner()
                self.two_living_fighters = False
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health <= 0:
                    self.winner = self.dinosaur.name
                    self.display_winner()
                    self.two_living_fighters = False
            
    def display_winner(self):
        print(f'The winner is {self.winner}!')
 
