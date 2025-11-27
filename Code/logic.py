from player import Player
from elements import *
from upgrades import *
from courbe import Courbe
import os

def highscore(new_score = 0, filename="highscore.txt"):
    """
    Updates highscore, returns new high score (can be used without arg to get current highscore)
    """
    try:
        with open(filename, "r") as f:
            stored_score = int(f.read().strip())
    except FileNotFoundError:
        stored_score = 0  # If no file yet, start at 0

    if new_score > stored_score:
        with open(filename, "w") as f:
            f.write(str(new_score))
        return new_score  # Updated
    else:
        return stored_score  # No change


class Game:
    def __init__(self):
        self.tick = 0
        self.day = 0
        self.daylenth = 5
        self.player = Player()
        self.kayou = Kayou(self.player,0.1)
        self.mps = 0
        self.impots = 0
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
        self.mps = self.player.mget()
        for item in self.elements.items() + self.upgrades.items() + self.share.items() + [self.kayou]: # + [self.event]
            item.update()
        self.mps = self.player.mget() - self.mps
        # End
        if self.player.mget() < 0:
            highscore(self.day)
            # appeller game end interface
            pass
    def buy(self,id,type):
        match type:
            case "kayou":
                self.kayou.buy()
            case "element":
                self.elements[id].buy()
            case "upgrade":
                self.elements[id].buy()
            case "share":
                self.share[id].buy()
    def sell(self,id,type):
        match type:
            case "kayou":
                self.kayou.sell()
            case "element":
                self.elements[id].sell()
            case "upgrade":
                self.elements[id].sell()
            case "share":
                self.share[id].sell()