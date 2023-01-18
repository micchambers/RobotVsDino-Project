class Battleground:

    def __init__(self, name):
        self.name = name

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to the " + self.name)

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
 
