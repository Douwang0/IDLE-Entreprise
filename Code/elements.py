from random import *
from player import Player

class Element:
    def __init__(self,player : Player,valeur):
        self.price = None # modify with randomifiers later
        self.qty = 0
        self.player = player
        self.marche = random()
    def update(self):
        pass
        # self.price
    def sell(self,nbr):
        """
        Sells nbr of elements, return false if not enough elements
        """
        if nbr > self.qty:
            return False
        else:
            self.player.madd(self.price*nbr)
            self.qty -= nbr
            return True
    def buy(self,nbr):
        if self.player.msub(nbr*self.price):
            self.qty += nbr
    def price_change(self):
        pass

class Share(Element):
    def __init__(self):
        super().__init__()
        self.rate = 0 # Change for random as well
    def update(self):
        super().update()
        self.dividend()
    def dividend(self):
        self.player.madd(self.rate*self.qty)

class Kayou(Element):
    def buy(self):
        self.qty +=1