from logic import Game

class Events():
    def __init__(self, index, eventtype, temp, duration):
        self.index = index
        self.enventtype = eventtype
        self.temp = temp
        self.duration = duration
    def action(self, game : Game):
        if self.enventtype == "kayou+":
            game.kayou.price *= self.temp
        elif self.enventtype == "timodif":
            game.daylenth += self.temp
        elif self.enventtype == "pricemodif":
            for i in game.elements:
                i.price += (i.price / 100) * self.temp
        elif self.enventtype == "employrendmodif":
            game.upgrades["employes"].bonus += (game.upgrades["employes"].bonus / 100) * self.temp
        elif self.enventtype == "demmandemodif":
            for i in game.elements:
                i.courbe.chance += self.temp
        elif self.enventtype == "gainjourinstant":
            game.player.madd(game.mps * game.daylenth * self.temp)
        elif self.enventtype == "taxmodif":
            game.impots += self.temp
        elif self.enventtype == "gainsmodif":
            game.elements.