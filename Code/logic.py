from player import Player
from elements import *
from upgrades import *
from courbe import Courbe

class Game:
    def __init__(self):
        self.tick = 0
        self.day = 0
        self.daylenth = 5
        self.player = Player()
        self.kayou = Kayou(self.player,0.1)
        # self.event = Eventmanagement()
        self.elements = {
        }
        self.upgrades = {
            "employes" : Employes()
        }
        self.share = {
        }
    def update(self):
        self.tick += 1
        if  self.tick >= self.daylenth:
            self.tick = 0
            self.day += 1
            # appeler game pause interface
        for item in self.elements.items() + self.upgrades.items() + self.share.items() + [self.kayou]: # + [self.event]
            item.update()
        # End
        if self.player.mget() < 0:
            # appeller game end interface
            pass
    def buy(self,id,type):
        pass
