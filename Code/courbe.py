from random import *
class Courbe:
    def __init__(self):
        self.var = random(randint(0, 1))
        self.event = 0
        self.evolution = 0
    def eventcourbe(self):
        self.event = random(randint(3, 6))
        self.evolution = random(randint(-1, 1))
    def update(self):
        if self.event == 0 :
            self.eventcourbe()
        else:
            self.var *= random(randint(0.01, 0.05)) * self.evolution
            self.event -= 1