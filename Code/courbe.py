"""
Docstring for courbe

Doit etre une coube dans laquelle on peut obtenir une variable aleatoire entre 0 et 1 
avec une alteration sur le mouvement de la courbe grace a une variable chance. 
La coube doit avoir une certaine stabilitee 
"""

import random as rand

class Courbe:
    def __init__(self):
        self.var = rand.uniform(0.05, 1)
        self.event = 0
        self.evolution = 0
        self.chance = 0
    def eventcourbe(self):
        # Durée de l'événement
        self.event = rand.randint(3, 6)

        # Biais central (évite de coller aux bords)
        center_bias = (0.5 - self.var) * 100

        # Biais total
        bias = self.chance + center_bias

        # Clamp du biais
        bias = max(-100, min(100, bias))

        # Tirage directionnel
        self.evolution = rand.choices(
            [-1, 1],
            [100 - bias, 100 + bias]
        )[0]

    def update(self):
        # Si aucun événement actif, on en crée un
        if self.event <= 0:
            self.eventcourbe()

        # Intensité du mouvement (très faible = stabilité)
        amplitude = rand.uniform(0.01, 0.1)

        # Application de l'évolution (+1 ou -1)
        self.var += amplitude * self.evolution

        # Clamp pour rester strictement entre 0 et 1
        if self.var < 0.05:
            self.var = 0.05
            self.evolution = 1
        elif self.var > 1:
            self.var = 1
            self.evolution = -1

        # On consomme l'événement
        self.event -= 1

    def getvar(self):
        return self.var
    def chancemodif(self, mod):
        """
        Docstring for chancemodif
        
        :param mod: Int entre -100 et 100, négatif = bas et positif = haut 
        """
        self.chance += mod

""" old
    def update(self):
        if self.event == 0 :
            self.eventcourbe()
        elif self.var < 0:
            self.evolution = 1
        elif self.var > 1:
            self.evolution = -1
        else:
            a = 1  * self.evolution
            b = 5  * self.evolution
            if a < b:
                self.var *= rand.randint(a, b) / 100
            else:
                self.var *= rand.randint(b, a) / 100
            self.event -= 1

"""