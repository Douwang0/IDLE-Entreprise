from joueur import *

class Employes():
    def __init__(self, price, bonus, player : Player):
        self.price = price
        self.bonus = bonus
        self.qty = 0
        self.player = player
        self.augment = 10
    def buy(self, nbr):
        if self.qty == 10 ^ self.augment :
            self.price *= 5
            self.augmentation()
        elif self.player.msub(self.price + 1.05 ^ nbr) and nbr + self.qty <= self.augment:
            self.qty += nbr
            self.price = self.price + 1.05 ^ nbr + 1
    def update(self):
        self.player.madd(self.qty * self.bonus)
    def augmentation(self):
        """
        Tous les multiples de 10 de nombre d'employers, le prix de ceux ci augmente mais il rapportent plus
        """
        if self.player.msub(self.price):
            self.bonus *= 5
            self.augment *= 10
    def rendmodif(self, mod):
        temp = self.bonus
        self.bonus += (self.bonus / 100) * mod
        return temp