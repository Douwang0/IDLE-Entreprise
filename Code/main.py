from logic import Game
from gui import UserInterface

class App:
    def __init__(self):
        self.game = Game()
        self.ui = UserInterface()

if __name__ == "__main__":
    App()
