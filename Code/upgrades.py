from joueur import *

class Employes():
    def __init__(self, price, bonus, player : Player):
        self.price = price
        self.bonus = bonus
        self.qty = 0
        self.player = player
        self.augment = 1
    def buy(self, nbr):
        if not (nbr > 10 * self.augment - self.qty):
            if self.player.msub(nbr*self.price):
                self.qty += nbr        
            if self.qty == 10 * self.augment :           
                self.augmentation()
        else:
            reste = nbr - (10 * self.augment - self.qty)
            self.buy(nbr-reste)
            self.buy(reste)
    def update(self):
        self.player.madd(self.qty * self.bonus) 
    def augmentation(self):
        """
        Tous les multiples de 10 de nombre d'employers, le prix de ceux ci augmente mais il rapportent plus
        """
        if self.player.msub(self.price):
            self.price *= 5
            self.bonus *= 5
            self.augment += 1
    def rendmodif(self, mod):
        temp = self.bonus
        self.bonus += (self.bonus / 100) * mod
        return temp