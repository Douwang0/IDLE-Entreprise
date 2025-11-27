import random as rand

class Courbe:
    def __init__(self):
        self.var = rand.randint(0, 1)
        self.event = 0
        self.evolution = 0
        self.chance = 0
    def eventcourbe(self):
        self.event = rand.randint(3, 6)
        self.evolution = rand.choices([-1,1], [100 - self.chance, 100 + self.chance])
    def update(self):
        if self.event == 0 :
            self.eventcourbe()
        else:
            self.var *= (rand.randint(1, 5) / 100) * self.evolution
            self.event -= 1
    def getvar(self):
        return self.var