import random as rand

class Courbe:
    def __init__(self):
        self.var = rand.randint(0, 1)
        self.event = 0
        self.evolution = 0
        self.chance = 0
    def eventcourbe(self):
        self.event = rand.randint(3, 6)
        self.evolution = rand.choices([-1,1], [100 - self.chance, 100 + self.chance])[0]
    def update(self):
        if self.event == 0 :
            self.eventcourbe()
        elif self.var < 0:
            self.evolution = 1
        elif self.var > 1:
            self.evolution = -1
        else:
            self.var *= rand.randint((1  * self.evolution), 5  * self.evolution) / 100
            self.event -= 1
    def getvar(self):
        return self.var
    def chancemodif(self, mod):
        """
        Docstring for chancemodif
        
        :param mod: Int entre -100 et 100, négatif = bas et positif = haut 
        """
        self.chance += mod