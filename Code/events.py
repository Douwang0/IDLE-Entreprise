from logic import Game
from upgrades import Employes


class Events:
    def __init__(self, index, temp, duration, desc, eventtype=[]):
        self.index = index
        self.enventtype = eventtype
        self.temp = temp
        self.duration = duration
        self.description = desc
    def action(self, game : Game):
        if "kayou+" in self.enventtype:
            game.kayou.price *= self.temp
        elif "timodif" in self.enventtype:
            game.daylenth += self.temp
        elif "pricemodif" in self.enventtype:
            self.temp = (game.elements[i].price / 100) * self.temp
            for i in game.elements:
                game.elements[i].price += self.temp
        elif "employrendmodif" in self.enventtype:
            self.temp = (game.upgrades["employes"].bonus / 100) * self.temp
            game.upgrades["employes"].bonus += self.temp
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
    def cancer(self, game : Game):
        if "timodif" in self.enventtype:
            game.daylenth -= self.temp
        elif "pricemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].price -= self.temp
        elif "employrendmodif" in self.enventtype:
            game.upgrades["employes"].bonus -= self.temp
        elif "demmandemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].courbe.chance -= self.temp
        elif "taxmodif" in self.enventtype:
            game.impots -= self.temp
        elif "gainsmodif" in self.enventtype:
            game.player.bonus -= self.temp / 100
        
        
        
        
        
    
def active_event(event:Events, game_ref:Game, gui_ref): #app enverra la référence à game
    event.action(game_ref)
    gui_ref.request_event_animation(event.description, 20.0)
    event.cancer(game_ref)

dic_event = {1 : Events(0, 100, 0, "La lune est percutée par un violent astéroïde, pluie de débris sur Terre : Les kayoux voient leur prix multiplié par 100", ["kayou+"]),
             2 : Events(1, 3, 180, "Cthulhu fait son retour : La nuit tombe durant 3 minutes", ["timodif"]),
             3 : Events(2, 20 ,300, "Macron fait son vingtième mandat : Le taux inflation augmente de 20 % pendant 5 jours", ["pricemodif"])}
