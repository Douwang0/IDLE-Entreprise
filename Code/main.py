from logic import Game
from gui import UserInterface

class App:
    def __init__(self):
        self.game = Game()
        self.ui = UserInterface()
        self.ui.set_game_ref(self.game)
        self.ui.run()
        
if __name__ == "__main__":
    App()