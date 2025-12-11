from player import Player
from elements import *
from upgrades import *
from courbe import Courbe

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
        self.player = Player(self)
        self.kayou = Kayou(self.player,0.1)
        self.mps = 0
        self.impots = 0.01
        self.benefices_journee = 0
        self.benefice_hier = 0
        self.quota = 10000
        # self.event = Eventmanagement()
        self.elements = {
            "stylo" : Element(self.player,5),
            "Bouteille" : Element(self.player,20),
            "Chaise" : Element(self.player,50),
            "Chaise (Sophistiquée)" : Element(self.player,800),
            "Samsung 2TM" : Element(self.player,500),
            "Ordinateur Fixe" : Element(self.player,4000),
            "Ordinateur Portatif" : Element(self.player,1500),
            "Ordinateur Quantique" : Element(self.player,3.2),
            "camionnnn" : Element(self.player,200000),
            "voiture (Sophistiquée)" : Element(self.player,500000),
            "Maison" : Element(self.player,800000),
            "The legend of Zelda Souvenir d'Enfance - Matthieu Meriot" : Element(self.player,5),
            "Planètes": Element(self.player, 1e8),
            "gachettes pour manettes": Element(self.player, 36),
            'des touches "cap lock"': Element(self.player, 280),
            "de pixel": Element(self.player, 700000),
            "éléments de surprise": Element(self.player, 8e10),
            "Mona Lisa": Element(self.player, 16),
            "la lettre alpha": Element(self.player, 1200),
            "cheveux de Frida Kaloh": Element(self.player, 98000),
            "iphon XX": Element(self.player, 2.5),
            "chemise de Charles": Chemise(self.player, "tres cher"),
            "boeing 732": Element(self.player, 70000),
            "être humain de droite": Element(self.player, 12000),
            "La chaine Vilbrequin": Element(self.player, 5000000)
        }
        self.upgrades = {
            "employes" : Employes(100,10,self.player)
        }
        self.allcollectebles = self.elements.items() + self.upgrades.items() + [self.kayou]
        self.allIterable = self.allcollectebles # + [self.event]
    def update(self):
        self.tick += 1
        self.mps = self.player.mget()
        for item in self.allIterable:
            item.update()
        self.mps = self.player.mget() - self.mps
        # End
        if  self.tick >= self.daylenth:
            self.new_day()
        if self.player.mget() < 0:
            highscore(self.day)
            # appeller game end interface
    def buy(self,id,type,nbr = 1):
        match type:
            case "kayou":
                self.kayou.buy()
            case "element":
                self.elements[id].buy(nbr)
            case "upgrade":
                self.elements[id].buy(nbr)
            case "share":
                self.share[id].buy(nbr)
    def sell(self,id,type,nbr = 1):
        match type:
            case "kayou":
                return self.kayou.sell(nbr)
            case "element":
                return self.elements[id].sell(nbr)
            case "upgrade":
                return self.elements[id].sell(nbr)
            case "share":
                return self.share[id].sell(nbr)
    def new_day(self):
            self.tick = 0
            impots = (self.benefices_journee * self.impots) if self.benefices_journee > 0 else 0
            self.benefice_hier = self.benefices_journee
            self.benefices_journee = 0
            self.player.msub(impots,True)
            self.player.msub(self.quota*self.impots,True)
            self.day += 1
            self.impots *= 1.05
            # appeler game pause interface
        