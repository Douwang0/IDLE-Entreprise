from logic import *

class Player:
    def __init__(self,game : Game):
        self.game = game
        self.__argent = 0
    def mget(self):
        return self.__argent
    def madd(self,nbr):
        self.__argent += nbr
        self.game.benefices_journee += nbr
    def msub(self,nbr,force = False) -> bool:
        """
        Return affordability and subtract nbr from money, if false, cancel transaction
        """
        if nbr > self.__argent and force is False:
            return False
        else:
            self.__argent -= nbr
            self.game.benefices_journee -= nbr
            return True