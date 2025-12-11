from random import *
from joueur import *
from courbe  import *

class Element:
    def __init__(self,player : Player,valeur):
        self.price = valeur
        self.qty = 0
        self.player = player
        self.courbe = Courbe()
        self.valeur = valeur
    def update(self):
        self.courbe.update()
        self.price = self.valeur * self.courbe.getvar() * 2
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
        if not 0 < nbr <= 100:
            return
        if self.player.msub(nbr*self.price):
            self.qty += nbr

class Kayou(Element):
    def buy(self):
        self.qty +=1

class Chemise(Element):
    def __init__(self,player,value):
        self.player = player
        self.price = 0
        pass
    def update(self):
        self.price = self.player.mget() + 1
    def buy(self,nbr):
        pass