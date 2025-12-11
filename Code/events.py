from logic import *
from upgrades import *

class Events:
    def __init__(self, index, temp, duration, eventtype=[]):
        self.index = index
        self.enventtype = eventtype
        self.temp = temp
        self.duration = duration
    def action(self, game : Game):
        if "kayou+" in self.enventtype:
            game.kayou.price *= self.temp
        elif "timodif" in self.enventtype:
            game.daylenth += self.temp
        elif "pricemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].price += (game.elements[i].price / 100) * self.temp
        elif "employrendmodif" in self.enventtype:
            game.upgrades["employes"].bonus += (game.upgrades["employes"].bonus / 100) * self.temp
        elif "demmandemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].courbe.chance += self.temp
        elif "gainjourinstant" in self.enventtype:
            game.player.madd(game.mps * game.daylenth * self.temp)
        elif "taxmodif" in self.enventtype:
            game.impots += self.temp
        elif "gainsmodif" in self.enventtype:
            game.player.bonus += self.temp / 100
        elif "aliens" in self.enventtype:
            game.upgrades["Alien"] = Employes(100,20,game.player)
        elif "newevent" in self.enventtype:
            pass
    
def active_event(event:Events, game_ref:Game): #app enverra la référence à game
    event.action(game_ref)
    