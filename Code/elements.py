"""
elements.py

Module contenant les classes représentant les objets achetables
et revendables dans le jeu.

Chaque élément possède :
- un prix
- une quantité
- une courbe d'évolution de valeur
"""

from joueur import Player
from courbe import Courbe


class Element:
    """
    Classe représentant un élément du marché.

    Un élément peut être acheté, vendu et voit son prix évoluer
    selon une courbe aléatoire.
    """

    def __init__(self, player: Player, valeur):
        self.price = valeur          # Prix actuel
        self.valeur = valeur         # Valeur de base
        self.qty = 0                 # Quantité possédée
        self.player = player
        self.courbe = Courbe()

    def update(self):
        """
        Met à jour le prix de l'élément en fonction de la courbe.
        """
        self.courbe.update()
        self.price = self.valeur * self.courbe.getvar() * 2

    def sell(self, nbr):
        """
        Vend un nombre donné d'éléments.

        Paramètres
        ----------
        nbr : int
            Quantité à vendre

        Retour
        ------
        bool
            False si la quantité est insuffisante, True sinon
        """
        if nbr > self.qty:
            return False

        self.player.madd(self.price * nbr)
        self.qty -= nbr
        return True

    def buy(self, nbr):
        """
        Achète un nombre donné d'éléments si le joueur a assez d'argent.
        """
        if not 0 < nbr <= 100:
            return

        if self.player.msub(nbr * self.price):
            self.qty += nbr
    def pricemodif(self, mod): #en pourcentages
        temp = self.price
        self.price += (self.price/100) * mod
        return temp
    def instaget(self, nb):
        self.qty += nb


class Kayou(Element):
    """
    Élément spécial achetable à l'unité.
    """

    def buy(self):
        """
        Achète un Kayou (quantité +1).
        """
        self.qty += 1


class Chemise(Element):
    """
    Élément particulier dont le prix dépend directement
    de l'argent du joueur.
    """

    def __init__(self, player, value):
        self.player = player
        self.price = 0

    def update(self):
        """
        Met à jour le prix en fonction de l'argent du joueur.
        """
        self.price = self.player.mget() + 1

    def buy(self, nbr):
        """
        Achat non implémenté (élément spécial).
        """
        pass
