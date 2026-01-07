from logic import *
from upgrades import *
from random import *

class Events:
    def __init__(self,index, dispo:bool, temp, duration, desc, eventtype=[]):
        self.index = index
        self.dispo = dispo
        self.enventtype = eventtype
        self.temp = temp
        self.temp2 = [0]
        self.duration = duration
        self.description = desc
    def action(self, game : Game, dic):
        dic_event = dic
        if "kayou+" in self.enventtype:
            game.kayou.pricemodif(self.temp) 
        elif "timodif" in self.enventtype:
            game.timemodif(self.temp)
        elif "pricemodif" in self.enventtype:
            a = 0
            for i in game.elements:
                self.temp2[a] = game.elements[i].pricemodif(self.temp)
                a += 1    
        elif "employrendmodif" in self.enventtype:
            game.upgrades["employes"].rendmodif(self.temp)
        elif "demmandemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].courbe.chancemodif(self.temp[1])
        elif "gainjourinstant" in self.enventtype:
            game.player.madd(game.mps * game.daylenth * self.temp)
        elif "taxmodif" in self.enventtype:
            game.taxmodif(self.temp[0])
        elif "gainsmodif" in self.enventtype:
            game.player.bonusmodif(self.temp[0] / 100)
        elif "aliens" in self.enventtype:
            game.upgrades["Alien"] = Employes(100,20,game.player)
        elif "newevent" in self.enventtype:
            dic_event[self.temp[1]].dispo = True
        elif "cancevent" in self.enventtype:
            dic_event[self.temp[2]].dispo = False
        elif "gaininstant" in self.enventtype:
            game.player.madd(self.temp)
        elif "pertemoitierinstant" in self.enventtype:
            game.player.divisargent()
        elif "gainparts" in self.enventtype:
            for i in game.elements:
                game.elements[i].instantget(self.temp)
    def delete(self, game : Game,dic):
        dic_event = dic
        if "timodif" in self.enventtype:
            game.daylenth -= self.temp
        elif "pricemodif" in self.enventtype:
            a = 0
            for i in game.elements:
                game.elements[i].pricemodif(self.temp2[a])
                a += 1    
        elif "employrendmodif" in self.enventtype:
            game.upgrades["employes"].rendmodif(-(self.temp))
        elif "demmandemodif" in self.enventtype:
            for i in game.elements:
                game.elements[i].courbe.chancemodif(- (self.temp))
        elif "taxmodif" in self.enventtype:
            game.taxmodif(-(self.temp[0]))
        elif "gainsmodif" in self.enventtype:
            game.player.bonusmodif(-(self.temp / 100))
        
class EventManager:
    def __init__(self,game):
        self.game = game
        self.event = None
        self.timer = 10 #randint(180,240) seul le premier arrive en 10 sec
        self.gui = None
        self.pending_event = []
        self.dic_event = {1 : Events(1, True, 9900, 0, "La lune est percutée par un violent astéroïde, pluie de débris sur Terre : Les kayoux voient leur prix multiplié par 100", ["kayou+"]),
                    2 : Events(2, True, 3, 180, "Cthulhu fait son retour : La nuit tombe durant 3 minutes", ["timodif"]),
                    3 : Events(3, True, -20 ,300, "Macron fait son vingtième mandat : Le taux inflation augmente de 20 % pendant 5 jours", ["pricemodif"]), 
                    4 : Events(4, True, 10, 0, "Sébastien Lecornu est promu premier ministre pour la 227ième fois : les employés sont plus efficaces de 10 %", ["employrendmodif"]),
                    5 : Events(5, True, [0, -50], 60, "Les cavaliers de la mort marchent sur Paris : La demande sur le marché diminue de 50 % pour le jour", ["demmandemodif"]),
                    6 : Events(6, True, 200, 0, "Pastek, le roi des 11 ciels, donne sa faveur à l'entreprise : gain instantané de 200 pourcents des gains touchés le jour précédent", ["gainjourinstant"]),
                    7 : Events(7, True, [0.1] , 60, "Une ampoule a grillé chez l'URSAF: payez 10 pourcents d'impôts en plus à la fin de la journée", ["taxmodif"]),
                    8 : Events(8, True, 100, 0, "Restock mondial de ciao Kombucha : les employers travaillent deux fois plus efficacement", ["employrendmodif"]),
                    9 : Events(9, True, [20, 10, 9], 0, "Jesus resucite : Vous gagnez 20 % plus d'argent", ["gainsmodif", "newevent", "cancevent"]),
                    10 : Events(10, False, [-20, 9, 10], 0, "Jésus est crucifié de nouveau : Vous perdez votre bonus de 20 pourcents de gains", ["gainsmodif","newevent","cancevent"]),
                    11 : Events(11, True, [-1, -100], 60, "Le Ragnarok débute : vous n'avez plus d'impôts ni de demande sur le marché pour ce jour", ["demmandemodif", "taxmodif"]),
                    12 : Events(12, True, [0, 0, 12], 0, "Les aliens débarquent : baisse du prix des employés", ["aliens", "cancevent"]),
                    13 : Events(13, True, 0, 0, "Il est lundi (ou pas jsp en vrai)", []),
                    14 : Events(14, True, [0, 15, 14], 0, "Vous découvrez que tout l'argent du monde vous a été promis il y a 3000 ans : Jérusalem est découverte", ["newevent", "cancevent"]),
                    15 : Events(15, False, [0, 16, 15], 0, "Annexion de Jérusalem : Vous pouvez vous évader fiscalement à Jérusalem", ["newevent", "cancevent"]),
                    16 : Events(16, False, [0], 0, "Evasion fiscale à Jérusalem : ne payez plus d'impôts", ["taxmodif"]),
                    17 : Events(17, True, 0, 0, "Les gilets jaunes font leur retours : le prix de l'essence augmente ", []),
                    18 : Events(18, True, [-0.1, 19, 18], 0, "Votre femme vous a trompé, elle prend les enfants et 50 pourcents de vos biens, vous devez maintenant payer la pension alimentaire jusqu'à votre mort.", ["pertemoitierinstant", "gainsmodif", "newevent", "cancevent"]),
                    19 : Events(19, False, [0, 20, 21], 0, "Vous découvrez la théorie de l'internet mort ", ["newevent", "cancevent"]),
                    20 : Events(20, False, [0, 21, 20], 0, "Vous publiez un article sur cette théorie et devenez connus", ["newevent", "cancevent"]),
                    21 : Events(21, False, [0.1, 22, 21], 0, "Votre femme revient", ["gainsmodif", "newevent", "cancevent"]),
                    22 : Events(22, False, [23, 22], 0, "Vous créez une IA pour mettre de la vie sur internet", ["newevent", "cancevent"]),
                    23 : Events(23, False, 13, 0, "l'IA contrôle internet : +13 pourcents de parts de marchées ", ["gainparts"]),
                    24 : Events(24, True, 0, 0, "Vous êtes de bonne humeur aujourd'hui", []),
                    25 : Events(25, True, 0, 0, "Contrôle fiscal (-50 pourcents d'argent)", ["pertemoitierinstant"]),
                    26 : Events(26, True, -7, 180, "La machine a boisson du groupe << ice team >> a cessé de fonctionné, baisse de production des empoyés de 7% pendant 3 jours", ["employrendmodif"]),
                    27 : Events(27, True, -10, 60, "Vous avez trop dormi, les employés on eu la flemme de travailler", ["employrendmodif"]),
                    28 : Events(28, True, 0, 0, "Il pleut", []),
                    29 : Events(29, True, 0, 0, "Vous êtes sur la liste d'Epstein", []),
                    30 : Events(30, True, 50, 180, "Livraison d'Ice Tea, 50 pourcents d'efficacité des employés en plus", ["employrendmodif"]),
                    31 : Events(31, True, 0, 0, "Votre fils est con", []),
                    32 : Events(32, True, 200, 0, "Vous passez par la case départ", ["gaininstant"]),
                    33 : Events(33, True, 2.5, 0, "Vous volez la carte vitale d'un employé", ["gaininstant"]),
                    34 : Events(34, True, 0, 0, "Un employé à lâché une caisse, il faut la réparer (-50 pourcents d'argent)", ["pertemoitierinstant"])}

    def active_event(self,event:Events, gui_ref): #app enverra la référence à game
        print("test_event")
        try:
            event.action(self.game,self.dic_event)
            gui_ref.game_screen.request_event_animation(event.description)
            if event.duration != 0:
                self.pending_event.append[event,event.duration]
        except Exception as e: print(e)

    def update(self):
        self.timer -=1
        for pending in self.pending_event:
            pending[1] -=1
            if pending[1] <= 0:
                pending[0].delete(self.game,self.dic_event)
                self.pending_event.remove(pending)
        if self.timer <= 0:
            self.timer = randint(180,240)
            event = self.dic_event[randint(1,34)]
            self.active_event(event,self.gui)
