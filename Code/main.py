from logic import *
from joueur import *
from elements import *
from upgrades import *
from courbe import *
from events import *
from gui import *

class App:
    def __init__(self):
        self.game = Game()
        self.ui = UserInterface()
        self.game.ui = self.ui
        self.ui.game = self.game
if __name__ == "__main__":
    App()
